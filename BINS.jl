using Base.Test

function search(n, L)
	low = 1
	high = length(L)
	while low <= high
		mid = int((low + high)/2)
		if n < L[mid]
			high = mid - 1
		elseif n > L[mid]
			low = mid + 1
		else
			return mid
		end
	end
	return -1
end

function main(n, m, A, B)
	result = ""
	for i in B
		if i != ""
			result = string(result, search(i, A), " ")
		end
	end
	return result[1:end-1]
end

function parse(filename)
	f = open(filename, "r")
	t = readdlm(f)

	n = t[1]
	m = t[2]
	A = t[3, :]
	B = t[4, :]

	return main(n, m, A, B)
end

@test parse("BINS.txt") == "4 1 -1 -1 4 2"