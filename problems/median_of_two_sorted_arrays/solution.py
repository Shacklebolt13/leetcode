class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        la = len(nums1)
        lb = len(nums2)
        s = la+lb
        
        if(s%2!=0):
            even = False
        else:
            even = True
            
        ptr = 0
        med = s//2 + 1
        lb -=1
        la -=1
        tmp = None
        while True:
            print(la,lb,ptr,med)
            if(la>=0 and lb>=0):  #comparable
                if(nums1[la]>=nums2[lb]):   #take a
                    ptr+=1
                    if(ptr==med):
                        if(even):
                            return (tmp + nums1[la])/2
                        else:
                            return nums1[la]
                        
                    elif(even and ptr==med-1):
                        tmp = nums1[la]
                    
                    la-=1
                else:   #take b
                    ptr+=1
                    if(ptr==med):
                        if(even):
                            return (tmp + nums2[lb])/2
                        else:
                            return nums2[lb]
                        
                    elif(even and ptr==med-1):
                        tmp = nums2[lb]
                    
                    lb-=1
                    
            elif(lb<0): #take a
                ptr+=1
                if(ptr==med):
                    if(even):
                        return (tmp + nums1[la])/2
                    else:
                        return nums1[la]

                elif(even and ptr==med-1):
                    tmp = nums1[la]

                la-=1
            
            else:   #take b
                ptr+=1
                if(ptr==med):
                    if(even):
                        return (tmp + nums2[lb])/2
                    else:
                        return nums2[lb]
                        
                elif(even and ptr==med-1):
                    tmp = nums2[lb]

                lb-=1
                    
                
                
        
            
        
            
            
        
        
        
            