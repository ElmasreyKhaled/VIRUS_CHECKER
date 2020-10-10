import validators


class check:
    def cheacking(inp):
        k = validators.domain(inp)
        if k is True:
            return "Domain"
        else:
            k = validators.ipv4(inp)
            h = validators.ipv6(inp)
            if k is True:
                return "IP"
            else:
                k = validators.url(inp)
                if k is True:
                    return "URL"
                else:
                    return "File_Hash"
