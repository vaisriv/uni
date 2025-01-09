import Pkg; Pkg.add("Symbolics")

using LinearAlgebra
using Symbolics

function clc()
    if Sys.iswindows()
        return read(run(`powershell cls`), String)
    elseif Sys.isunix()
        return read(run(`clear`), String)
    elseif Sys.islinux()
        return read(run(`printf "\033c"`), String)
    end
end

function tensor_lower(A::Matrix, eta::Matrix, rc::String)
    if rc == "r"
        return transpose(eta*transpose(A))
    end
    if rc == "c"
        return eta*A
    end
end

function tensor_upper(A::Matrix, eta::Matrix, rc::String)
    if rc == "r"
        return transpose(inv(eta)*transpose(A))
    end
    if rc == "c"
        return inv(eta)*A
    end
end

function symmetric_part(A::Matrix)
    return 1/2*(A+transpose(A))
end

function asymmetric_part(A::Matrix)
    return 1/2*(A-transpose(A))
end

