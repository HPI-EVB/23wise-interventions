mutable struct Gaussian
    μ::Float64
    σ2::Float64

    Gaussian(μ, σ2) =
        (σ2 <= 0) ? error("Variance must be greater than 0") :
        new(promote(μ, σ2)...)
end

function Gaussian()
    return Gaussian(0, 1)
end

function Base.show(io::IO, g::Gaussian)
    print(io, "μ = ", g.μ, ", σ2 = ", g.σ2)
end
