def LCM():
{
		multiple = 20
		sum=0

	while(sum==0):  
	{
		    if(multiple % 11 == 0 and multiple % 12 == 0 and multiple % 13 ==0 and multiple % 14 ==0
		   and multiple % 15 ==0 and multiple % 16 ==0 and multiple % 17 ==0 and multiple % 18 ==0
		   and multiple % 19 ==0 and multiple % 20 ==0):
		   {
			sum = multiple
            }
		     else
		    {
   			multiple = multiple + 20
		    }
		return sum
	}
}
print(LCM())