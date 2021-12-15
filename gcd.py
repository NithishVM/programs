# Python3 implementation of the above approach
from math import gcd

maxLen = 30;

# Array to store segment-tree
seg = [0] * (3 * maxLen);

# Function to build segment-tree to
# answer range GCD queries
def build(l, r, i, arr) :

	# Base-case
	if (l == r) :
		seg[i] = arr[l];
		return seg[i];

	# Mid element of the range
	mid = (l + r) // 2;

	# Merging the result of left and right sub-tree
	seg[i] = gcd(build(l, mid, 2 * i + 1, arr),
				build(mid + 1, r, 2 * i + 2, arr));
	return seg[i];

# Function to perform range GCD queries
def query(l, r, l1, r1, i) :

	# Base-cases
	if (l1 <= l and r <= r1) :
		return seg[i];
		
	if (l > r1 or r < l1) :
		return 0;

	# Mid-element
	mid = (l + r) // 2;

	# Calling left and right child
	return gcd(query(l, mid, l1, r1, 2 * i + 1),
			query(mid + 1, r, l1, r1, 2 * i + 2));

# Function to find the required count
def findCnt(arr, n) :

	# Building the segment tree
	build(0, n - 1, 0, arr);

	# Two pointer variables
	i = 0; j = 0;

	# To store the final answer
	ans = 0;

	# Looping
	while (i < n) :

		# Incrementing j till we don't get
		# a gcd value of 1
		while (j < n and
			query(0, n - 1, i, j, 0) != 1) :
			j += 1;

		# Updating the final answer
		ans += (n - j);

		# Increment i
		i += 1;

		# Update j
		j = max(j, i);

	# Returning the final answer
	return ans;

# Driver code
if __name__ == "__main__" :

	arr = [ 1, 1, 1, 1 ];
	n = len(arr);

	print(findCnt(arr, n));

# This code is contributed by AnkitRai01
# Python3 implementation of the above approach
from math import gcd

maxLen = 30;

# Array to store segment-tree
seg = [0] * (3 * maxLen);

# Function to build segment-tree to
# answer range GCD queries
def build(l, r, i, arr) :

	# Base-case
	if (l == r) :
		seg[i] = arr[l];
		return seg[i];

	# Mid element of the range
	mid = (l + r) // 2;

	# Merging the result of left and right sub-tree
	seg[i] = gcd(build(l, mid, 2 * i + 1, arr),
				build(mid + 1, r, 2 * i + 2, arr));
	return seg[i];

# Function to perform range GCD queries
def query(l, r, l1, r1, i) :

	# Base-cases
	if (l1 <= l and r <= r1) :
		return seg[i];
		
	if (l > r1 or r < l1) :
		return 0;

	# Mid-element
	mid = (l + r) // 2;

	# Calling left and right child
	return gcd(query(l, mid, l1, r1, 2 * i + 1),
			query(mid + 1, r, l1, r1, 2 * i + 2));

# Function to find the required count
def findCnt(arr, n) :

	# Building the segment tree
	build(0, n - 1, 0, arr);

	# Two pointer variables
	i = 0; j = 0;

	# To store the final answer
	ans = 0;

	# Looping
	while (i < n) :

		# Incrementing j till we don't get
		# a gcd value of 1
		while (j < n and
			query(0, n - 1, i, j, 0) != 1) :
			j += 1;

		# Updating the final answer
		ans += (n - j);

		# Increment i
		i += 1;

		# Update j
		j = max(j, i);

	# Returning the final answer
	return ans;

# Driver code
if __name__ == "__main__" :

	arr = [ 1, 1, 1, 1 ];
	n = len(arr);

	print(findCnt(arr, n));

# This code is contributed by AnkitRai01
