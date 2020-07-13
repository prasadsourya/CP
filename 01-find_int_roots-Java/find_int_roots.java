// # Write the function bonusFindIntRoots(a,b,c) that takes 
// # the int coefficients a, b, c of a quadratic equation of this form:
// #      y = ax2 + bx + c
// # You are guaranteed the function has 2 real roots, and in fact that 
// # the roots are all integers. Your function should return these 2 int roots as a list
// # in increasing order. How does a function return multiple values? Like so:
// # return root1, root2


class find_int_roots {
	public int[] fun_find_int_roots(int a, int b, int c){
		// your code goes here
		
		//int[] arr = {a,b,c};
		int x = (int)(-b + Math.sqrt(b*b - 4*a*c))/2*a;
		int y = (int)(-b - Math.sqrt(b*b - 4*a*c))/2*a;
		if (x>y) {
			int[] arr1 = {y,x};
			return arr1;
		} else {
			int[] arr2 = {x,y};
			return arr2;
		}
			
	}
	public static void main(String[] args) {
				
	}
}