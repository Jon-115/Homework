import unittest

def inverse(fileName):
    
    file = open(fileName,'r')
    newfile = str(file.read())
    file.close()

    file = open(fileName,'w+')

    for word in range(len(newfile)):
        if newfile[word].isupper():
            file.write(newfile[word].lower())
        elif newfile[word].islower():
            file.write(newfile[word].upper())
        else:
            file.write(newfile[word])
    
    #print(file.read())
    file.close()

    file = open(fileName,'r')
    print(file.read())
    file.close()
  
inverse('Homework/python/InterviewQuestions/old projects/week 4/readFile.txt')


# class Testfile(unittest.TestCase):

#     def testInverse(self):
#         self.assertEqual(inverse('Homework/python/InterviewQuestions/old projects/week 4/readFile.txt'))

# unittest.main()