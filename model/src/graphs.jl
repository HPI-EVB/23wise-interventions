include("gaussians.jl")
include("factors.jl")

# computes prediction for series subgraph
# input has rows μ, σ, time passed until next, columns are records
function evaluate_series(series::Matrix{Float64}, λ::Float64)::Gaussian
    if size(series)[1] != 3
        throw(ArgumentError("Input needs to have 3 rows"))
    end
    if length(series) == 0
        throw(ArgumentError("Series is empty"))
    end

    result = Gaussian(series[1,1], series[2,1])
    time_passed!(result, series[3, 1])

    for record = eachcol(series)
        result = weighted_sum(result, 1 - λ, Gaussian(record[1], record[2]), λ)
        time_passed!(result, record[3])
    end

    return result
end
