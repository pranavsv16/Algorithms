class patternMatching:

    def __init__(self):
        self.lps = []
        self.count =0
        self.indices=[]

    def kmpAlgorithm(self,pattern,text):
        self.computeLPS(pattern)
        m=len(pattern)
        n=len(text)

        i,j=0,0

        while i<n:

            if j<m and pattern[j]==text[i]:
                i=i+1
                j=j+1
            elif j==m:
                self.count=self.count+1
                self.indices.append(i-j)
                j=self.lps[j-1]
            else:
                if i<n and text[i]!=pattern[j]:
                    if j!=0:
                        j=self.lps[j-1]
                    else:
                        i=i+1
        if i==n and j==m:
            self.count=self.count+1
            self.indices.append(i-j)
        return self.count


    def computeLPS(self,pattern):

        length = len(pattern)
        j,i=0,1
        self.lps=[0]*length

        while i<length:
            if pattern[j]==pattern[i]:
                j=j+1
                self.lps[i]=j
                i=i+1
            else:
                if j!=0:
                    j=self.lps[j-1]
                else:
                    self.lps[i]=0
                    i=i+1


def main():
    kmp  = patternMatching()
    pattern = input()
    text =pattern()
    print(kmp.kmpAlgorithm(pattern,text))
    print(kmp.indices)
main()
