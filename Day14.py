
	# Add your code here
    def computeDifference(self):
        Max = -99
        for i in range(0,len(self.__elements)):
            for j in range(i+1 , len(self.__elements)):
                current = abs(self.__elements[i] - self.__elements[j])
                Max = max(current,Max)
        self.maximumDifference = Max