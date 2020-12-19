class Solution:
    def validIPAddress(self, IP) -> str:

        Addr = IP.split('.')
        if len(Addr) == 1:
            Addr = IP.split(':')
        if len(Addr) == 4:
            for i in Addr:
                if 1 <= len(i) <= 3 and i.isdigit() and 0 <= int(i) <= 255:
                    if len(i) > 1 and i[0] == "0":
                        return "Neither"
                    else:
                        continue
                else:
                    return "Neither"
            return "IPv4"

        elif len(Addr) == 8:
            print('8')
            for a in Addr:
                print(a)
                if 1 <= len(a) <= 4:
                    print('if')
                    for b in a:
                        print(b)
                        if b.isdigit():
                            continue
                        else:
                            if b not in 'abcdef' and b not in 'ABCDEF':
                                return 'Neither'
                            else:
                                continue
                else:
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'
