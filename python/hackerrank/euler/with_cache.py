
def with_cache(fn):
    cache_data = {}
    fn_name = fn.__name__

    def inner(x):
        if x in cache_data:
            R = cache_data[x]
            print(f"#{fn_name}: cache hit\n#\t{x}\n#\t{R}")
        else:
            # print(f"#{fn_name}: cache miss\n#\t{x}\n#\t?")
            R = fn(x)
            cache_data[x] = R
            print(f"#{fn_name}: cache fill\n#\t{x}\n#\t{R}")
        return R
    return inner

# USAGE:
#
# @with_cache
# def function_that_needs_cache(single_parameter):
