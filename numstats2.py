import statistics 

newCalculation = True;
while newCalculation:

    #sum = 0;
    #count = 0;
    fileName = str(input("What is the name of the file you want to open: "));
    try:
        f = open(fileName, "r");
        #print("list of random numbers in random.txt: ");
        #max = 0;
        #min = 10;
        numbers = []
        for x in f:
            #print(x)
            #num = int(x)
            
            numbers.append(int(x));
            count2 = len(numbers)
            max2 = max(numbers)
            min2 = min(numbers)
            sum2= sum(numbers)
            #print("numbers ", numbers);
            #sum += int(x);
            #count += 1;
            average = sum2 / count2;
            range = max2 - min2;
       
        numbers.sort();
        
        length = len(numbers)
        if (length % 2 == 0):
            median = (numbers[(length)//2] + numbers[(length)//2-1]) / 2
        else:
            median = numbers[(length-1)//2]
        mode2 = max(numbers, key=lambda n: numbers.count(n))
        print("FileName: ", fileName);
        print("Sum: ", sum2);
        print("count: ",count2);
        print("Average: ", average);
        print("Max: ", max2);
        print("Min: ", min2);
        print("Range: ", range);
        print("Median: ", median);
        print("Mode: ", mode2);
   
   
        again = input("If you want to play again type y: ");
        if again != "y":
            newCalculation = False;
   
    except IOError:
        print("There is no file named randomnum.txt");

        if (len(numbers) < 1):
            print("the file is empty");

    


  
