
import numpy as np


class matrx:

    B = 0

    x1 = 3
    x2 = 4
    x3 = 5
    x4 = 6
    x5 = 7

    # main method called in main to run
    def run(self, obj):
        self.problem_two()

    # how to design problem two
    # x1 to x5 can be any real number
    # iterate as x1x2 x2x3 x3x4
    # in the next child node take one of x1orx2 and make sure you subtract .25 from the one you are taking as contraint
    # and you can also add .25 on the other one
    # make sure you check Z is equal to parent node Z not less if less stop there back track
    # if equal or better go deeper
    #     but stop when you have an integer x1 and x2 (thats integer solution) and check Z answer

    def branch_bound(self, var1, var2, prev_Z, status, status_l_r, position):
        # position is for choosing the variable you want to proceed with in main -
        # you have choice to either computer using var_a (x1) or var_b(x2)

        # status_l_r is what side you want to compute if you put 'left' you are going towards
        # less than x1 in that case you subtract 0.25 but if you put 'right' you are going torwards
        # x2 that is greater than in which you add

        # first check the var for the constraints being sent are ints or not
        # if ints calc the z and thats it you cannot solve furter
        # if float go ahead but only if its value is Z or greater

        # c1 =  isinstance(var1, int)
        # c2 = isinstance(var2, int)
        var1 = float(var1)
        var2 = float(var2)
        c1 = (var1).is_integer()
        c2 = (var2).is_integer()

        if c1 and c2:   # have reached integer state
            #print(var1 , " ->" , c1 , " | " , var2 , " ->" , c2 , " | Status:" , status_l_r )
            new_Z = self.objective_function(var1, var2, status)
            #print('prev: ', prev_Z)
            #print('new Z: ', new_Z)
            if new_Z >= prev_Z:
                return new_Z

        else:

            if self.constraint(var1, var2, status) == True:
                if status_l_r == 'left':  # status_l_r - left is going on node and checking for less equal
                    # in branch bound method
                    new_Z = self.objective_function(var1, var2, status)
                    if new_Z >= prev_Z:
                        if position == 'var_a':
                            return self.branch_bound(float(float(var1) - 0.25), float(var2), new_Z, status,
                                                     status_l_r, position)
                        if position == 'var_b':
                            return self.branch_bound(var1, float(float(var2) - 0.25), new_Z, status, status_l_r,
                                                     position)
                    else:
                        return -1  # 'Not searching further'

                if status_l_r == 'right':  # status_l_r - right is going on the right node and checking for less equal
                    # in branch bound method
                    new_Z = self.objective_function(var1, var2, status)
                    # print("in right -> passing new vars:", var1, " , ", float(float(var2) + 0.25))
                    # print("prev : ", prev_Z)
                    # print("new ", new_Z)
                    if new_Z >= prev_Z:
                        # print("True")
                        if position == 'var_a':
                            return self.branch_bound(float(float(var1) + 0.25), float(var2), new_Z, status,
                                                     status_l_r, position)
                        if position == 'var_b':
                            return self.branch_bound(var1, float(float(var2) + 0.25), new_Z, status, status_l_r,
                                                     position)
                        return self.branch_bound(float(float(var1) + 0.25), float(var2), new_Z, status, 'right')
                    else:
                        return -1  # 'Not searching further'

            else:
                #print("infeasible as it goes above the constraint")
                return prev_Z


            # if status_l_r == 'left':    # status_l_r - left is going on node and checking for less equal
            #     # in branch bound method
            #     if self.constraint(var1, var2, status) == True:
            #         new_Z = self.objective_function(var1, var2, status)
            #         if new_Z >= prev_Z:
            #             if position == 'var_a':
            #                 return self.branch_bound( float(float(var1) - 0.25), float(var2), new_Z, status, status_l_r,position)
            #             if position == 'var_b':
            #                     return self.branch_bound( var1, float(float(var2) - 0.25), new_Z, status, status_l_r,position)
            #         else:
            #             return -1 # 'Not searching further'
            #
            # if status_l_r == 'right':   # status_l_r - right is going on the right node and checking for less equal
            #     # in branch bound method
            #     if self.constraint(var1, var2, status) == True:
            #         new_Z = self.objective_function(var1, var2, status)
            #         print("in right -> passing new vars:", var1, " , ", float(float(var2) + 0.25))
            #         print("prev : ", prev_Z)
            #         print("new ", new_Z)
            #         if new_Z >= prev_Z:
            #             # print("True")
            #             if position == 'var_a':
            #                 return self.branch_bound( float(float(var1) + 0.25), float(var2), new_Z, status, status_l_r, position)
            #             if position == 'var_b':
            #                 return self.branch_bound( var1, float(float(var2) + 0.25), new_Z, status, status_l_r, position)
            #             return self.branch_bound( float(float(var1) + 0.25), float(var2), new_Z, status,'right')
            #         else:
            #             return -1 # 'Not searching further'
            #     else:
            #         print("infeasible as it goes above the constraint")
            #         return prev_Z


            # if status_l_r == 'left':
            #     if self.constraint(var1, var2, status) == True:
            #         new_Z = self.objective_function(var1, var2, status)
            #         #print("Z left  prev :", prev_Z)
            #         #print("Z left  new :", new_Z)
            #         if new_Z >= prev_Z:
            #             if position == 'var_a':
            #                 return self.branch_bound( float(float(var1) - 0.25), float(var2), new_Z, status, 'left')
            #             if position == 'var_b':
            #                     return self.branch_bound(float(float(var1) - 0.25), float(var2), new_Z, status, 'left')
            #         else:
            #             #print("Else statement Z left :" , prev_Z)
            #             return -1 # 'Not searching further'
            # if status_l_r == 'right':
            #     #print('in right: ' , prev_Z)
            #     if self.constraint(var1, var2, status) == True:
            #         new_Z = self.objective_function(var1, var2, status)
            #         #print('in right -> new Z: ', new_Z)
            #         if new_Z >= prev_Z:
            #             # print("in right -> passing new vars:" , float(float(var1) + 0.25) , " , " , var2)
            #             return self.branch_bound( float(float(var1) + 0.25), float(var2), new_Z, status,'right')
            #         else:
            #             #print("Z right :", prev_Z)
            #             return -1 # 'Not searching further'





    def problem_two(self):
        # here we iterate and divide into tree like this
        # (x1,x2,x3,x4,x5) = x1x2 x2x3 x3x4 x4x5
        Z = self.objective_function(self.x1, self.x2, 'var1')
        # var_a = self.x1
        # var_b =self.x2

        # There should be two branch_bound - left and right | left being less and right being greater
        # its up to you if you want to make changes to x1 or x2 in my case i chose x1

        # print("x1 :", self.x1 ,"| x2 :", self.x2 ,"| x3 :", self.x3 ,"| x4 :", self.x4 ,"| x5 :", self.x5)

        var1 = var2 = var3 = var4 = 0

        # x1 x2
        var_a = self.x1
        var_a  = float(var_a)
        var_b = self.x2
        var_b = float(var_b)
        left_x1 = self.branch_bound( (var_a - 0.25) , var_b, Z,'var1' , 'left', 'var_a')
        right_x1 = self.branch_bound( (var_a + 0.25), var_b, Z, 'var1', 'right', 'var_a')
        left_x2 = self.branch_bound( var_a , (var_b - 0.25), Z,'var1' , 'left', 'var_b')
        right_x2 = self.branch_bound( var_a, (var_b+ 0.25), Z, 'var1', 'right', 'var_b')
        #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
        print("left_x1 (main) :" , left_x1 )
        print("right_x1 (main):", right_x1)
        print("left_x2 (main) :" , left_x2 )
        print("right_x2 (main):", right_x2)

        # x2 x3
        var_a = self.x2
        var_a  = float(var_a)
        var_b = self.x3
        var_b = float(var_b)
        left_x1 = self.branch_bound( (var_a - 0.25) , var_b, Z,'var1' , 'left', 'var_a')
        right_x1 = self.branch_bound( (var_a + 0.25), var_b, Z, 'var1', 'right', 'var_a')
        left_x2 = self.branch_bound( var_a , (var_b - 0.25), Z,'var1' , 'left', 'var_b')
        right_x2 = self.branch_bound( var_a, (var_b+ 0.25), Z, 'var1', 'right', 'var_b')
        # var2 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
        print("x2x3")
        print("left_x1 (main) :" , left_x1 )
        print("right_x1 (main):", right_x1)
        print("left_x2 (main) :" , left_x2 )
        print("right_x2 (main):", right_x2)

        



    def objective_function(self,var_a,var_b, status):
        # ( 1 * x1 ) + ( 2 * x2 ) + ( 3 * x3 ) + ( 4 * x4 ) + ( 5 * x5 )
        if status == 'var1':    #x1x2
            Z = ( 1 * var_a ) + ( 2 * var_b ) + ( 3 * self.x3 ) + ( 4 * self.x4 ) + ( 5 * self.x5 )

        if status == 'var2':    #x2x3
            Z = ( 1 * self.x1 ) + ( 2 * var_a ) + ( 3 * var_b ) + ( 4 * self.x4 ) + ( 5 * self.x5 )

        if status == 'var3':    #x3x4
            Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * var_a ) + ( 4 * var_b ) + ( 5 * self.x5 )

        if status == 'var4':    #x4x5
            Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * self.x3 ) + ( 4 * var_a ) + ( 5 * var_b )

        if status == 'main':    #x4x5
            Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * self.x3 ) + ( 4 * self.x4 ) + ( 5 * self.x5 )

        return Z

    def constraint(self,var_a,var_b, status):
        if status == 'var1':    #x1x2
            constraint = (5 * pow(var_a, 2)) + (45 * pow(var_b, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(self.x5, 2))

        if status == 'var2':    #x2x3
            constraint = (5 * pow(self.x1, 2)) + (45 * pow(var_a, 2)) + (3 * pow(var_b, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(self.x5, 2))

        if status == 'var3':    #x3x4
            constraint = (5 * pow(self.x1, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(var_a, 2)) + (2 * pow(var_b, 2)) + (1 * pow(self.x5, 2))

        if status == 'var4':    #x4x5
            constraint = (5 * pow(self.x1, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(var_a, 2)) + (1 * pow(var_b, 2))

        if constraint <= 1000:
            return True
        return False

def main():
    m = matrx()
    m.run(m)

if __name__ == '__main__':
    main()

