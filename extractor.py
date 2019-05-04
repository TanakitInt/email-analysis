import os

def extract():
    #extract an email list into new csv file (comma delimited)

    #enter file name *The file must have the same directory with this python script and must be .csv file*
    print("Please enter file name (with extension) : ")
    fileName = str(input())

    with open(fileName) as file:
        email = file.read()
        email = email.replace('\r', '').replace('\n', '')
        email = email.split(",")

        #box1 contains a list in the list
        box1 = []
        for i in email:
            i = i.split("@")
            box1.append(i)

        #box2 contains a list mixed with name and email provider
        box2 = []
        for j in box1:
            for k in j:
                box2.append(k)

        #box3 contains only email provider in the list
        box3 = []

        box3 = box2[1::2]

    #create new directory
    if not os.path.exists("output"):
        os.makedirs("output")

    #write into new .csv file
    with open("output/emailProvider.csv", 'w') as output:
        output.write("email_provider" + ","+ "\n")
        for i in box3:
            output.write(i + "," + "\n")

    #write into new .txt file
    with open("output/emailProvider.txt", 'w') as output:
        output.write("email_provider" + ","+ "\n")
        for i in box3:
            output.write(i + ","+ "\n")

extract()
