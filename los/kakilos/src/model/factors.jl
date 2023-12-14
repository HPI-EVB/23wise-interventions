include("gaussians.jl")

function weighted_sum(g1::Gaussian, a1::Float64, g2::Gaussian, a2::Float64)::Gaussian
    Gaussian(
        a1 * g1.μ + a2 * g2.μ,
        a1^2 * g1.σ2 + a2^2 * g2.σ2
    )
end

function time_passed!(g::Gaussian, t::Float64)
    g.μ -= t
end
