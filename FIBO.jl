using Base.Test

function fib(x)
    if x == 0
        return 0
    elseif x == 1
        return 1
    else
        return fib(x-1) + fib(x-2)
    end
end

@test fib(6) == 8
println(fib(25))
