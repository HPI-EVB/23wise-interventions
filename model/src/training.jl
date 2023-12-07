include("gaussians.jl")
include("factors.jl")
include("graphs.jl")

# cost as value of log of density
function cost(prediction::Gaussian, label::Float64)::Float64
    1/2 * log(2 * π * prediction.σ2) + (label - prediction.μ)^2 / (2 * prediction.σ2)
end

function cost(predictions::Vector{Gaussian}, labels::Vector{Float64})::Float64
    sum(cost.(predictions, labels))
end
