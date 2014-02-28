# This program will eventually implement a solution for the project euler problem 98

def happify(n):
        while True:
                # pdb.set_trace()
                if n == 1 or n == 89:
                        steps.append(n)
                        break
                sumOfSquares = 0
                for i in str(n):
                        sumOfSquares += int(i)**2
                steps.append(sumOfSquares)
                n = sumOfSquares
        # print str(steps)
        return n

for i in range(1, 101):
        steps = [i]
        if happify(i) == 89:
                print "Loops: " + str(steps)
        else:
                print "Halts: " + str(steps)
