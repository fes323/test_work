class Solution:
    stack = []

    def push(self, item):
        self.stack.append(item)

    def pop_first(self):
        return self.stack.pop(0)

    def pop_last(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def simplifyPath(self, path: str) -> str:
        # Заполняем стек
        for i in path:
            self.stack.append(i)

        new_stack = []
        counter = 0
        while self.size(self):
            x = self.pop_first(self)
            new_stack.append(x)
            if len(new_stack) > 0:
                last_x = new_stack[len(new_stack) - 1]

            if last_x == '.':
                counter += 1
            if last_x != '.' and len(new_stack) > 1:
                if counter >= 1 and counter < 3:
                    data = new_stack[len(new_stack) - 1]
                    for i in range(counter+1):
                        new_stack.pop()
                    new_stack.append(data)
                    counter = 0

                continue

        dataPath = ''.join(map(str, new_stack))
        while True:
            dataPath = dataPath.replace('//', '/')
            if '//' not in dataPath:
                break
        if dataPath.endswith('/'):
            dataPath = dataPath[:len(dataPath)-1]
        if not dataPath.startswith('/'):
            dataPath = '/'+dataPath
        print(dataPath)


Solution.simplifyPath(Solution, path='/home//foo')