import numpy as np
import matplotlib.pyplot as plt

def step_gradient(b_current, w_current, train_x, train_y, learning_rate):
    b = 0
    w = 0
    m = len(train_y)
    global K
    global B
    for i in range(m):
        x = train_x[i]
        y = train_y[i]
        b += (1/m) * (((w_current * x) + b_current) - y)
        w += (1/m) * x * (((w_current * x) + b_current) - y)
        b_new = b_current - (learning_rate * b)
        w_new = w_current - (learning_rate * w)
        B=b_new
        K=w_new
    return [b_new, w_new]


def run_descent(train_x, train_y, init_b, init_w, epochs, learning_rate):
    b = init_b
    w = init_w
    for i in range(epochs):
        b, w = step_gradient(b, w, train_x, train_y, learning_rate)
    return [b, w,]



def drawPlot(train_x, train_y, m, b):
    plt.plot(train_x, train_y, 'ro')
    plt.plot([0, 7000], [0 + b, 7000*m + b], color='b', linestyle='-', linewidth=2)
    plt.xlabel('averageRating')
    plt.ylabel('numVotes')
    plt.tight_layout()
    plt.show()


def run():
    file = 'data1.csv'
    points = np.array(np.genfromtxt(file, delimiter=',', skip_header=1))
                      
    learning_rate = 0.0000001  

    train_x = points[:,1]  
    train_y = points[:,2]
    init_b = 0
    init_w = 0

    print('{} - number of training examples'.format(len(train_y)))
    print('k = 0, b = 0 | initial parameters')

    epochs = 10
    [b, w] = run_descent(train_x, train_y, init_b, init_w, epochs, learning_rate)

    print('k = {}, b = {} | final parameters'.format(w, b))
    m = len(train_y)
    drawPlot(train_x, train_y, w, b)


if __name__ == '__main__':
    run()
'''
from tkinter import *
def prePrice():
    amt=float(amount.get())
    itrt=float(intRate.get())
    lo=float(ty.get())
    yrs=float(years.get())
    y=((K*amt)+(K1*itrt)+(K2*yrs)+(K3*lo)+B)
    lblMonthly=Label(main, text = 'Rs %.2f' % y).grid(row=5,column=1,padx=0,pady=10)
    return
main = Tk()
main.title("House Price Prediction")
main.geometry('700x700')
 
amount = StringVar()
intRate = StringVar()
years = StringVar()
ty = StringVar()
 
lblAmount = Label(main, text = 'Enter the size of house :').grid(row = 0, column = 0, padx = 0, pady = 10)
entAmount = Entry(main, textvariable = amount).grid(row = 0, column = 1)
 
lblIntRate = Label(main, text = 'Enter the number of bedroom :').grid(row = 1, column = 0, padx = 0, pady = 10)
entIntRate = Entry(main, textvariable = intRate).grid(row = 1, column = 1)
 
lblYears = Label(main, text = 'Enter the number of bolcony :').grid(row = 2, column = 0, padx = 0, pady = 10)
entYears = Entry(main, textvariable = years).grid(row = 2, column = 1)  

city = Label(main, text = ' The number for corresponding city Hydrabad=1, Kolkata=2, Bengaluru=3, Delhi=4, Mumbai=5:').grid(row = 3, column = 0, padx = 0, pady = 10)
cityName = Label(main, text = 'Enter the number of City :').grid(row = 4, column = 0, padx = 0, pady = 10)
cityNo = Entry(main, textvariable = ty).grid(row = 4, column = 1)

btn= Button(main,text='calculate', command= prePrice).grid(row=6, column=1)

lblMonthly = Label(main, text ='Predict Price is : ').grid(row=5,column=0,padx=0,pady=10)

main.mainloop()'''
