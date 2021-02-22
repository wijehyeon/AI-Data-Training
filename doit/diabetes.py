from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

print(diabetes.data.shape, diabetes.target.shape)

print(diabetes.data[0:3])
print(diabetes.target[:3])

x = diabetes.data[:,2]
y = diabetes.target

w = 1.0
b = 1.0


y_hat = x[0] * w + b

print(y_hat)

print(y[0])


# translate weight
w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b
print(y_hat_inc)