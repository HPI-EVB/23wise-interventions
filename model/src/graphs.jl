include("gaussians.jl")
include("factors.jl")

# computes prediction for series subgraph
function evaluate_series(
    μs::Vector{Float64},  # mean values
    σ2s::Vector{Float64}, # sigma values
    ts::Vector{Float64},  # time to next record or end
    λ::Float64,           # weight
)::Gaussian
    result = Gaussian(μs[1], σ2s[1])
    time_passed!(result, ts[1])

    for (μ, σ2, t) = zip(μs, σ2s, ts)
        result = weighted_sum(result, 1 - λ, Gaussian(μ, σ2), λ)
        time_passed!(result, t)
    end

    return result
end
