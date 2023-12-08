include("gaussians.jl")
include("factors.jl")
include("graphs.jl")

# cost as value of negative log of density
function cost(prediction::Gaussian, label::Float64)::Float64
    1/2 * log(2 * π * prediction.σ2) + (label - prediction.μ)^2 / (2 * prediction.σ2)
end

function cost(predictions::Vector{Gaussian}, labels::Vector{Float64})::Float64
    sum(cost.(predictions, labels))
end

function rbf(x1::Float64, x2::Float64, σ2::Float64)::Float64
    exp((x1 - x2)^2 / 2 * σ2)
end

# pseudo gradient descent without derivatives
function gradient_descent(
    x::Vector{Matrix{Float64}}, # vector are series, matrix columns are samples, rows are normalized value and time passed until next
    y::Vector{Float64},         # labels
    δ::Float64,  # step size to "evaluate partial derivate"
    γ::Float64,  # learning rate
    ϵ::Float64,  # convergence
    n::Float64,  # max iterations
    σ2::Float64, # rbf relationship of values
)::Tuple{Float64, Float64, Vector{Matrix{Float64}}} # final cost, λ, means & variances for each series
    # series flattened into 1
    x_flat = hcat(x...)
    # all flat normalized values
    values = x_flat[1,:]
    # kernel matrix for each possible pair of values
    kernel = rbf.(values', values, σ2)
    # all flat times
    times = x_flat[2, :]

    # bounds in flattened data for reconstruction
    bottom = 1
    bounds::Vector{UnitRange{Int64}} = []
    for series in x
        top = min(length(values), bottom + size(series)[2])
        push!(bounds, bottom:top)
        bottom = top + 1
    end

    # find initial values
    initial_μ, initial_σ2, λ = rand(3)
    # mean and sigma are multiplied with kernel to get correct initial distributions
    μs = initial_μ .* kernel[1, :]
    σ2s = initial_σ2 .* kernel[1, :]

    # cost for given parameters
    function evaluate_cost(μs::Vector{Float64}, σ2s::Vector{Float64}, λ::Float64)::Float64
        predictions = [evaluate_series(μs[b], σ2s[b], times[b], λ) for b in bounds]
        cost(predictions, y)
    end

    # ACTUAL GRADIENT DESCENT
    rate = γ / δ # learning rate
    current_cost = -100 # fine as initial value because cost is always positive
    for _ in 1:n
        # update cost & check if we have converged
        old_cost = current_cost
        current_cost = evaluate_cost(μs, σ2s)
        if abs(old_cost - current_cost) < ϵ break end
        # UPDATE PARAMETERS ALONG GRADIENT
        # we check the difference a small step (δ) would make,
        # scale it by 1/δ to get the gradient, multiply with the learning rate
        # and finally add it to the current value -> step downwards
        μs +=  [rate * (current_cost - evaluate_cost(μs + δ * kernel[i,:], σ2s)) for i in 1:length(values)]
        σ2s += [rate * (current_cost - evaluate_cost(μs, σ2s + δ * kernel[i,:])) for i in 1:length(values)]
        λ += rate * (current_cost - evaluate_cost(μs, σ2s, λ + δ))
    end

    # return value transformed back into original shape
    return (current_cost, lambda, [Matrix(hcat(μs[b], σ2s[b])') for b in bounds])
end
