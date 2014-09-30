class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		carr = 1
		for k in range(len(digits)-1, -1, -1):
			s = digits[k]+carr
			digits[k] = s if s<10 else 0
			carr = 0 if s<10 else 1
			if carr == 0:
				break
		if carr == 1:
			digits = [1] + digits
		return digits

print Solution().plusOne([9,9,9])
