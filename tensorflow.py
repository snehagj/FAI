import tensorflow as tf

print("TensorFlow Version:", tf.__version__)

# Define constants
x = tf.constant(10)
y = tf.constant(5)
z = tf.constant([2, 4, 6])

# Perform operations
sum_result = tf.add(x, y)
product_result = tf.multiply(x, y)
division_result = tf.divide(x, y)
squared = tf.square(z)
doubled = tf.multiply(z, 2)
condition_result = tf.cond(x > y, lambda: x - y, lambda: y - x)

# Print results
print("Sum:", sum_result.numpy())
print("Product:", product_result.numpy())
print("Division:", division_result.numpy())
print("Original Tensor:", z.numpy())
print("Squared:", squared.numpy())
print("Doubled:", doubled.numpy())
print("Condition Result:", condition_result.numpy())
