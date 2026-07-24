# 165. Compare Version Numbers
# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

# Example 1:
# Input: version1 = "1.2", version2 = "1.10"
# Output: -1
# Explanation:
# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

def compare_version_numbers(version1,version2):
    ver1 = version1.split(".")
    ver2 = version2.split(".")
    if len(ver1) > len(ver2):
        while len(ver1) > len(ver2):
            ver2.append("0")
    else : 
        while len(ver1) < len(ver2):
            ver1.append("0")
    for i in range(len(ver1)):
        if int(ver1[i]) < int(ver2[i]):
            return -1
        elif int(ver1[i]) > int(ver2[i]):
            return 1
    return 0 

print(compare_version_numbers("1.01","1.001"))