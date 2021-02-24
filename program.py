
class ParenthesisVerifier:
    def __init__(self):
        self.parenthesis_opened = "([{"
        self.parenthesis_closed = ")]}"

    def verify(self, string) -> bool:
        if len(string) == 0:
            return False
        if len(string) % 2 != 0:
            return False
        stack = []
        for c in string:
            if c in self.parenthesis_opened:
                stack.append(c)
            elif (i := self.parenthesis_closed.find(c)) != -1:
                if len(stack) == 0:
                    return False
                if self.parenthesis_opened.find(stack[-1]) != i:
                    return False
                stack.pop()
            else:
                return False
            
        return True

if __name__ == "__main__":
    verifier = ParenthesisVerifier()
    string = "([]){}"
    r = verifier.verify(string)
    if r == True:
        print("String is valid")
    else:
        print("String is not valid")