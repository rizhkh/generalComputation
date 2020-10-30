
import numpy as np


class matrx:

    B = 0

    x1 = 1
    x2 = 2
    x3 = 5
    x4 = 3
    x5 = 7

    # x1 = 12.9
    # x2 = 11
    # x3 = 10.8
    # x4 = 13.9
    # x5 = 14

    # x1 = 10
    # x2 = 11
    # x3 = 7
    # x4 = 8
    # x5 = 9

    prev_val_cosntraint_val = []
    obj_func_list = []

    # main method called in main to run
    def run(self, obj):

        self.problem_two_single_var()
        #self.problem_two()

    # how to design problem two
    # x1 to x5 can be any real number
    # iterate as x1x2 x2x3 x3x4
    # in the next child node take one of x1orx2 and make sure you subtract .25 from the one you are taking as contraint
    # and you can also add .25 on the other one
    # make sure you check Z is equal to parent node Z not less if less stop there back track
    # if equal or better go deeper
    #     but stop when you have an integer x1 and x2 (thats integer solution) and check Z answer

    def branch_bound_single_var(self, passed_list, obj_count, constraint_count,status_l_r,prev_val_obj_func, prev_val_cosntraint_func):

        # we can try single car branch bound where we try to find better obj funct
        # alpha is the point you start with
        # alpha add is the number you add in recursive
        # var1 includes [var1, obj_funct val]
        # my approach: first solve for x1 upto  a point where when you backtrack then you back track with new x1 value
        # now you have x1 value use that same x1 value in x2 but just solve for x2
        # and so on

        # c1 =  isinstance(var1, int)
        # c2 = isinstance(var2, int)
        var1 = passed_list[1]
        prev_Z = passed_list[0]
        var1 = float(var1)
        c1 = (var1).is_integer()

        if c1:  # have reached integer state
            # print( var1, " is integer")
            print(passed_list , " --------#######################>" , c1 , " | Status:" , status_l_r )
            Z_val = prev_Z
            new_Z = self.obj_funct(prev_val_obj_func, obj_count , var1)

            if new_Z >= prev_Z:
                nZ = [new_Z, float(float(var1))]
                return nZ

        else:
            if self.prev_val_cosntraint_val:
                prev_val_cosntraint_func = self.prev_val_cosntraint_val[-1]

            if self.constraint_single_var(prev_val_cosntraint_func, constraint_count, var1) <= 1000:
                if status_l_r == 'left':  # status_l_r - left is going on node and checking for less equal

                    new_Z = self.obj_funct(prev_val_obj_func, obj_count , var1)

                    # print("in left | passing new vars:", float(float(var1) - 0.25))
                    # print("prev : ", prev_Z)
                    # print("new ", new_Z)
                    if new_Z >= prev_Z:
                        nZ = [new_Z, float(float(var1) - 0.25)]
                        # print("new and going deeper ", new_Z)
                        return self.branch_bound_single_var(nZ, obj_count, constraint_count, 'left', prev_val_obj_func, prev_val_cosntraint_func)
                    else:
                        # print(" Left - objective func small going back")
                        return passed_list  # 'Not searching further'

                if status_l_r == 'right':  # status_l_r - right is going on the right node and checking for less equal
                    # in branch bound method
                    new_Z = self.obj_funct(prev_val_obj_func, obj_count , var1)
                    # print("in right | passing new vars:", float(float(var1) + 0.25))
                    # print("prev : ", prev_Z)
                    # print("new ", new_Z)
                    if new_Z >= prev_Z:
                        nZ = [new_Z, float(float(var1) + 0.25)]
                        # print("new and going deeper ", new_Z)
                        return self.branch_bound_single_var(nZ, obj_count, constraint_count, 'left', prev_val_obj_func, prev_val_cosntraint_func)
                    else:
                        # print(" Right - objective func small going back")
                        return passed_list  # 'Not searching further'
            else:
                print("infeasible as it goes above the constraint | Status:", status_l_r)
                return passed_list

    def obj_funct(self, prev_val, count, variable):
        # ( 1 * x1 ) + ( 2 * x2 ) + ( 3 * x3 ) + ( 4 * x4 ) + ( 5 * x5 )
        # print("in obj funct-----------------------------")
        # print(prev_val , " + " , count , "*",variable)
        Z = prev_val + count * variable
        return Z

    def constraint_single_var(self, prev_val, count, variable):
        constraint = 1500
        # print("in constraint_single_var funct &&&&&&&&&&&&&&&&&&&")
        # print(prev_val , " + " , count , "*",pow(variable,2))
        constraint = prev_val + count*pow(variable,2)
        return constraint

    def problem_two_single_var(self):
        # here we iterate in just single x e.g x1 x2 x3
        # and obj function is calculated by using the numbers from branch bound method

        # There should be two branch_bound - left and right | left being less and right being greater
        # its up to you if you want to make changes to x1 or x2 in my case i chose x1

        # print("x1 :", self.x1 ,"| x2 :", self.x2 ,"| x3 :", self.x3 ,"| x4 :", self.x4 ,"| x5 :", self.x5)


        # Z = self.x1
        # var_a = self.x1
        # var_a = float(var_a)
        # optimizer_var = 'x1'
        # x1_neg = [Z, var_a]
        # obj_count = 1
        # constraint_count = 5
        # prev_val_obj_func = 0
        # prev_val_cosntraint_func = 0
        # left_x1 = self.branch_bound_single_var([Z, var_a - 0.25], obj_count, constraint_count, 'left', 1, 0.1 , prev_val_obj_func, prev_val_cosntraint_func)
        #                                       #([Z, var_a - 0.25],       1,                  5,     'left', 1(alpha), 0.1(alpha),  0,                  0)
        #                                       #(passed_list,       obj_count, constraint_count, status_l_r,    alpha,  alpha_add, prev_val_obj_func,  prev_val_cosntraint_func)
        # right_x1 = self.branch_bound_single_var([Z, var_a + 0.25], obj_count, constraint_count, 'right', 1, 0.1 , prev_val_obj_func, prev_val_cosntraint_func)
        # # var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
        # print()
        # print('[ processing x1]')
        # print('[Obj func val, Varialbe = x1]')
        # print("left_x1 (main) :", left_x1)
        # print("right_x1 (main):", right_x1)

        i = 1
        cc =5
        increment = 6

        var_list = []

        self.obj_func_list.append(0)
        Z = self.x1
        while i<6:
            var_a = increment
            var_a = float(var_a)
            obj_count = i
            constraint_count = cc
            prev_val_obj_func = self.obj_func_list.pop()
            prev_val_cosntraint_func = 0
            left_x1 = self.branch_bound_single_var([Z, var_a - 0.25], obj_count, constraint_count, 'left', prev_val_obj_func, prev_val_cosntraint_func)
            right_x1 = self.branch_bound_single_var([Z, var_a + 0.25], obj_count, constraint_count, 'right', prev_val_obj_func, prev_val_cosntraint_func)
            print()
            print('[ processing ', increment , "]")
            print('[Obj func val, Variable = x1]')
            print("left_x1 (main) :", left_x1)
            print("right_x1 (main):", right_x1)
            if left_x1[0] > right_x1[0]:
                max = left_x1[0]
            else:
                max = right_x1
            print("444444444444444444444444444444444max val: ", max)
            constraint_count = cc * max[1]
            self.prev_val_cosntraint_val.append(constraint_count)
            obj = obj_count * max[1]
            self.obj_func_list.append(obj)
            z = max[0]

            cc = cc - 1
            i += 1
            increment += 1
            var_list.append(max[1])

        # j = 1
        # for i in var_list:
        #     o = j*i
        #     print
        #     sum = sum + o
        #     j += 1
        # print(sum)
        o = var_list[0] + 2*var_list[1] + 3*var_list[2] + 4*var_list[3] + 5*var_list[4]
        c = 5*pow( var_list[0],2) + 4*pow(var_list[1] ,2) + 3*pow( var_list[2],2) + 2*pow( var_list[3],2) + 1*pow(var_list[4] ,2)

        print("constraint : " , c)
        print("obj : " , o)

        if c<=1000:
            print("ozzzzzzzzzzzzzzbj : ", o)




    ############################################

#
# ##### THIS WORKS BUT NOT SURE IF I NEED THIS ONE BELOW ################
#
#
#     def branch_bound_single_var(self, passed_list, opt_func, status_l_r, alpha, alpha_add):
#         # we can try single car branch bound where we try to find better obj funct
#         # alpha is the point you start with
#         # alpha add is the number you add in recursive
#         # var1 includes [var1, obj_funct val]
#         # my approach: first solve for x1 upto  a point where when you backtrack then you back track with new x1 value
#         # now you have x1 value use that same x1 value in x2 but just solve for x2
#         # and so on
#
#         # c1 =  isinstance(var1, int)
#         # c2 = isinstance(var2, int)
#         var1 = passed_list[1]
#         prev_Z = passed_list[0]
#         var1 = float(var1)
#         c1 = (var1).is_integer()
#
#
#         if c1:   # have reached integer state
#             # print( var1, " is integer")
#             # print(passed_list , " -------->" , c1 , " | Status:" , status_l_r )
#
#             Z_val = prev_Z
#             new_Z = self.objective_function_single_var(Z_val, opt_func)
#             if new_Z >= prev_Z:
#                 nZ = [new_Z, float(float(var1))]
#                 return nZ
#
#         else:
#             if self.constraint_single_var(var1, opt_func) == True:
#                 if status_l_r == 'left':  # status_l_r - left is going on node and checking for less equal
#                     # in branch bound method
#                     new_Z = self.objective_function_single_var(var1, opt_func)
#                     # print("in left | passing new vars:", float(float(var1) + 0.25))
#                     # print("prev : ", prev_Z)
#                     # print("new ", new_Z)
#                     if new_Z >= prev_Z:
#                         nZ = [new_Z, float(float(var1) - 0.25)]
#                         # print("new and going deeper ", new_Z)
#                         return self.branch_bound_single_var( nZ, opt_func,status_l_r, alpha + alpha_add,alpha_add)
#                     else:
#                         # print(" Left - objective func small going back")
#                         return passed_list  # 'Not searching further'
#
#                 if status_l_r == 'right':  # status_l_r - right is going on the right node and checking for less equal
#                     # in branch bound method
#                     new_Z = self.objective_function_single_var(var1, opt_func)
#                     # print("in right | passing new vars:", float(float(var1) + 0.25))
#                     # print("prev : ", prev_Z)
#                     if new_Z >= prev_Z:
#                         nZ = [new_Z, float(float(var1) + 0.25)]
#                         # print("new ", new_Z)
#                         return self.branch_bound_single_var( nZ, opt_func,status_l_r, alpha + alpha_add,alpha_add)
#                     else:
#                         # print(" Right - objective func small going back")
#                         return passed_list  # 'Not searching further'
#             else:
#                 print("infeasible as it goes above the constraint | Status:" , status_l_r )
#                 return passed_list
#
#     def objective_function_single_var(self,var_a,status):
#         # ( 1 * x1 ) + ( 2 * x2 ) + ( 3 * x3 ) + ( 4 * x4 ) + ( 5 * x5 )
#         if status == 'x1':    #x1x2
#             Z = ( 1 * var_a ) + ( 2 * self.x2 ) + ( 3 * self.x3 ) + ( 4 * self.x4 ) + ( 5 * self.x5 )
#
#         if status == 'x2':    #x2x3
#             Z = ( 1 * self.x1 ) + ( 2 * var_a ) + ( 3 * self.x3 ) + ( 4 * self.x4 ) + ( 5 * self.x5 )
#
#         if status == 'x3':    #x3x4
#             Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * var_a ) + ( 4 * self.x4 ) + ( 5 * self.x5 )
#
#         if status == 'x4':    #x4x5
#             Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * self.x3 ) + ( 4 * var_a ) + ( 5 * self.x5 )
#
#         if status == 'x5':    #x4x5
#             Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * self.x3 ) + ( 4 * self.x4 ) + ( 5 * var_a )
#         return Z
#
#     def constraint_single_var(self,var_a, status):
#         constraint = 1500
#         if status == 'x1':    #x1x2
#             constraint = (5 * pow(var_a, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(self.x5, 2))
#             # if constraint <= 1000:
#             #     print("Constraint : ", constraint)
#
#         if status == 'x2':    #x2x3
#             constraint = (5 * pow(self.x1, 2)) + (45 * pow(var_a, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(self.x5, 2))
#             # if constraint <= 1000:
#             #     print("Constraint : ", constraint)
#
#         if status == 'x3':    #x3x4
#             constraint = (5 * pow(self.x1, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(var_a, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(self.x5, 2))
#             # if constraint <= 1000:
#             #     print("Constraint : ", constraint)
#
#         if status == 'x4':    #x4x5
#             constraint = (5 * pow(self.x1, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(var_a, 2)) + (1 * pow(self.x5, 2))
#             # if constraint <= 1000:
#             #     print("Constraint : ", constraint)
#         if status == 'x5':    #x4x5
#             constraint = (5 * pow(self.x1, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(var_a, 2))
#
#
#         if constraint <= 1000:
#             return True
#         return False
#
#     def constraint_calc_single_var(self,var_a,var_b,var_c,var_d,var_e):
#         constraint = 1500
#         constraint = (5 * pow(var_a, 2)) + (45 * pow(var_b, 2)) + (3 * pow(var_c, 2)) + (2 * pow(var_d, 2)) + (1 * pow(var_e, 2))
#         return constraint
#
#     def objfunc_calc_single_var(self, var_a, var_b, var_c, var_d, var_e):
#         # ( 1 * x1 ) + ( 2 * x2 ) + ( 3 * x3 ) + ( 4 * x4 ) + ( 5 * x5 )
#         Z = (1 * var_a) + (2 * var_b) + (3 * var_c) + (4 * var_d) + (5 * var_e)
#         return Z
#
#     def problem_two_single_var(self):
#         # here we iterate in just single x e.g x1 x2 x3
#         # and obj function is calculated by using the numbers from branch bound method
#
#
#         # There should be two branch_bound - left and right | left being less and right being greater
#         # its up to you if you want to make changes to x1 or x2 in my case i chose x1
#
#         # print("x1 :", self.x1 ,"| x2 :", self.x2 ,"| x3 :", self.x3 ,"| x4 :", self.x4 ,"| x5 :", self.x5)
#
#         var1 = var2 = var3 = var4 = 0
#
#         # x1 x2
#         st = self.constraint_single_var(var1, 'x1')
#         if st == True:
#             Z = self.objective_function_single_var(self.x1, 'x1')
#
#             var_a = self.x1
#             var_a  = float(var_a)
#             optimizer_var = 'x1'
#             x1_neg = [Z,var_a]
#             left_x1 = self.branch_bound_single_var( [Z,var_a - 0.25], optimizer_var , 'left', 1, 0.1)
#             right_x1 = self.branch_bound_single_var( [Z,var_a + 0.25] ,optimizer_var, 'right', 1, 0.1)
#             #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
#             print()
#             print( '[ processing x1]' )
#             print('[Obj func val, Varialbe = x1]')
#             print("left_x1 (main) :" , left_x1 )
#             print("right_x1 (main):", right_x1)
#             if left_x1[0]> right_x1[0]:
#                 max = left_x1[0]
#             else:
#                 max = right_x1
#             print("max val: " , max)
#
#             # x2
#             var_a = self.x2
#             var_a  = float(var_a)
#             optimizer_var = 'x2'
#             x1_neg = [Z,var_a]
#             left_x2 = self.branch_bound_single_var( [Z,var_a - 0.25], optimizer_var , 'left', 1, 0.1)
#             right_x2 = self.branch_bound_single_var( [Z,var_a + 0.25] ,optimizer_var, 'right', 1, 0.1)
#             #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
#             print()
#             print( '[ processing x2]' )
#             print('[Obj func val, Varialbe = x2]')
#             print("left_x2 (main) :" , left_x2 )
#             print("right_x2 (main):", right_x2)
#             if left_x2[0]> right_x2[0]:
#                 max2 = left_x2[0]
#             else:
#                 max2 = right_x2
#             print("max val: " , max2)
#
#             # x3
#             var_a = self.x3
#             var_a  = float(var_a)
#             optimizer_var = 'x3'
#             x1_neg = [Z,var_a]
#             left_x3 = self.branch_bound_single_var( [Z,var_a - 0.25], optimizer_var , 'left', 1, 0.1)
#             right_x3 = self.branch_bound_single_var( [Z,var_a + 0.25] ,optimizer_var, 'right', 1, 0.1)
#             #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
#             print()
#             print( '[ processing x3]' )
#             print('[Obj func val, Varialbe = x3]')
#             print("left_x3 (main) :" , left_x3 )
#             print("right_x3 (main):", right_x3)
#             if left_x3[0]> right_x3[0]:
#                 max3 = left_x3[0]
#             else:
#                 max3 = right_x3
#             print("max val: " , max3)
#
#             # x4
#             var_a = self.x4
#             var_a  = float(var_a)
#             optimizer_var = 'x4'
#             left_x4 = self.branch_bound_single_var( [Z,var_a - 0.25], optimizer_var , 'left', 1, 0.1)
#             right_x4 = self.branch_bound_single_var( [Z,var_a + 0.25] ,optimizer_var, 'right', 1, 0.1)
#             #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
#             print()
#             print( '[ processing x4]' )
#             print('[Obj func val, Varialbe = x4]')
#             print("left_x4 (main) :" , left_x4 )
#             print("right_x4 (main):", right_x4)
#             if left_x4[0]> right_x4[0]:
#                 max4 = left_x4[0]
#             else:
#                 max4 = right_x4
#             print("max val: " , max4)
#
#             # x5
#             var_a = self.x5
#             var_a  = float(var_a)
#             optimizer_var = 'x5'
#             left_x5 = self.branch_bound_single_var( [Z,var_a - 0.25], optimizer_var , 'left', 1, 0.1)
#             right_x5 = self.branch_bound_single_var( [Z,var_a + 0.25] ,optimizer_var, 'right', 1, 0.1)
#             #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
#             print()
#             print( '[ processing x5]' )
#             print('[Obj func val, Varialbe = x5]')
#             print("left_x5 (main) :" , left_x5 )
#             print("right_x5 (main):", right_x5)
#             if left_x5[0]> right_x5[0]:
#                 max5= left_x5[0]
#             else:
#                 max5 = right_x5
#             print("max val: " , max5)
#
#             print()
#             c = self.constraint_calc_single_var(max[1],max2[1],max3[1],max4[1],max5[1])
#             print( "constraint val: " , self.constraint_calc_single_var(max[1],max2[1],max3[1],max4[1],max5[1]) )
#             if c<=1000:
#                 Z = self.objfunc_calc_single_var(max[1],max2[1],max3[1],max4[1],max5[1])
#                 print( "obj: " , Z)
#
# #############################################


    # using lagragian function we simply unified our objective function and constraint function
    # we already know that for lambda u >= so we can simply select x^* as the min value in objective function

    def branch_bound(self, var1, var2, prev_Z, opt_func, status_l_r, position):
        # position is for choosing the variable you want to proceed with in main -
        # you have choice to either computer using var_a (x1) or var_b(x2)

        # opt_func is the 'x1x2' for the optimizer function

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
            new_Z = self.objective_function(var1, var2, opt_func)
            #print('prev: ', prev_Z)
            #print('new Z: ', new_Z)
            if new_Z >= prev_Z:
                return new_Z

        else:

            if self.constraint(var1, var2, opt_func) == True:
                if status_l_r == 'left':  # status_l_r - left is going on node and checking for less equal
                    # in branch bound method
                    new_Z = self.objective_function(var1, var2, opt_func)
                    if new_Z >= prev_Z:
                        if position == 'var_a':
                            return self.branch_bound(float(float(var1) - 0.25), float(var2), new_Z, opt_func,
                                                     status_l_r, position)
                        if position == 'var_b':
                            return self.branch_bound(var1, float(float(var2) - 0.25), new_Z, opt_func, status_l_r,
                                                     position)
                    else:
                        return -1  # 'Not searching further'

                if status_l_r == 'right':  # status_l_r - right is going on the right node and checking for less equal
                    # in branch bound method
                    new_Z = self.objective_function(var1, var2, opt_func)
                    # print("in right -> passing new vars:", var1, " , ", float(float(var2) + 0.25))
                    # print("prev : ", prev_Z)
                    # print("new ", new_Z)
                    if new_Z >= prev_Z:
                        # print("True")
                        if position == 'var_a':
                            return self.branch_bound(float(float(var1) + 0.25), float(var2), new_Z, opt_func,
                                                     status_l_r, position)
                        if position == 'var_b':
                            return self.branch_bound(var1, float(float(var2) + 0.25), new_Z, opt_func, status_l_r,
                                                     position)
                        return self.branch_bound(float(float(var1) + 0.25), float(var2), new_Z, opt_func, 'right')
                    else:
                        return -1  # 'Not searching further'

            else:
                #print("infeasible as it goes above the constraint")
                return prev_Z

    # this contains alpha value
    # def branch_bound(self, var1, var2, prev_Z, opt_func, status_l_r, position, alpha):
    #     # position is for choosing the variable you want to proceed with in main -
    #     # you have choice to either computer using var_a (x1) or var_b(x2)
    #
    #     # opt_func is the 'x1x2' for the optimizer function
    #
    #     # status_l_r is what side you want to compute if you put 'left' you are going towards
    #     # less than x1 in that case you subtract 0.25 but if you put 'right' you are going torwards
    #     # x2 that is greater than in which you add
    #
    #     # first check the var for the constraints being sent are ints or not
    #     # if ints calc the z and thats it you cannot solve furter
    #     # if float go ahead but only if its value is Z or greater
    #
    #     # c1 =  isinstance(var1, int)
    #     # c2 = isinstance(var2, int)
    #     var1 = float(var1)
    #     var2 = float(var2)
    #     c1 = (var1).is_integer()
    #     c2 = (var2).is_integer()
    #
    #     if c1 and c2:   # have reached integer state
    #         #print(var1 , " ->" , c1 , " | " , var2 , " ->" , c2 , " | Status:" , status_l_r )
    #         new_Z = self.objective_function(var1, var2, opt_func)
    #         new_Z = new_Z * alpha
    #         #print('prev: ', prev_Z)
    #         #print('new Z: ', new_Z)
    #         if new_Z >= prev_Z:
    #             return new_Z
    #
    #     else:
    #
    #         if self.constraint(var1, var2, opt_func) == True:
    #             if status_l_r == 'left':  # status_l_r - left is going on node and checking for less equal
    #                 # in branch bound method
    #                 new_Z = self.objective_function(var1, var2, opt_func)
    #                 new_Z = new_Z * alpha
    #                 if new_Z >= prev_Z:
    #                     if position == 'var_a':
    #                         return self.branch_bound(float(float(var1) - 0.25), float(var2), new_Z, opt_func,
    #                                                  status_l_r, position, alpha+0.1)
    #                     if position == 'var_b':
    #                         return self.branch_bound(var1, float(float(var2) - 0.25), new_Z, opt_func, status_l_r,
    #                                                  position, alpha+0.1)
    #                 else:
    #                     return -1  # 'Not searching further'
    #
    #             if status_l_r == 'right':  # status_l_r - right is going on the right node and checking for less equal
    #                 # in branch bound method
    #                 new_Z = self.objective_function(var1, var2, opt_func)
    #                 new_Z = new_Z * alpha
    #                 # print("in right -> passing new vars:", var1, " , ", float(float(var2) + 0.25))
    #                 # print("prev : ", prev_Z)
    #                 # print("new ", new_Z)
    #                 if new_Z >= prev_Z:
    #                     # print("True")
    #                     if position == 'var_a':
    #                         return self.branch_bound(float(float(var1) + 0.25), float(var2), new_Z, opt_func,
    #                                                  status_l_r, position, alpha+0.1)
    #                     if position == 'var_b':
    #                         return self.branch_bound(var1, float(float(var2) + 0.25), new_Z, opt_func, status_l_r,
    #                                                  position)
    #                     return self.branch_bound(float(float(var1) + 0.25), float(var2), new_Z, opt_func, 'right', alpha+0.1)
    #                 else:
    #                     return -1  # 'Not searching further'
    #
    #         else:
    #             #print("infeasible as it goes above the constraint")
    #             return prev_Z


    def problem_two(self):
        # here we iterate and divide into tree like this
        # (x1,x2,x3,x4,x5) = x1x2 x2x3 x3x4 x4x5
        # var_a = self.x1
        # var_b =self.x2

        # There should be two branch_bound - left and right | left being less and right being greater
        # its up to you if you want to make changes to x1 or x2 in my case i chose x1

        # print("x1 :", self.x1 ,"| x2 :", self.x2 ,"| x3 :", self.x3 ,"| x4 :", self.x4 ,"| x5 :", self.x5)

        var1 = var2 = var3 = var4 = 0

        # x1 x2
        st = self.constraint(var1, var2, 'x1x2')
        print(st)
        if st == True:

            Z = self.objective_function(self.x1, self.x2, 'x1x2')
            d = np.diff(Z)
            print(d)

            #x1x2
            var_a = self.x1
            var_a  = float(var_a)
            var_b = self.x2
            var_b = float(var_b)
            optimizer_var = 'x1x2'
            left_x1 = self.branch_bound( (var_a - 0.25) , var_b, Z, optimizer_var , 'left', 'var_a')
            right_x1 = self.branch_bound( (var_a + 0.25), var_b, Z, optimizer_var, 'right', 'var_a')
            left_x2 = self.branch_bound( var_a , (var_b - 0.25), Z, optimizer_var, 'left', 'var_b')
            right_x2 = self.branch_bound( var_a, (var_b+ 0.25), Z, optimizer_var, 'right', 'var_b')
            #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
            print()
            print( 'x1x2' )
            print("left_x1 (main) :" , left_x1 )
            print("right_x1 (main):", right_x1)
            print("left_x2 (main) :" , left_x2 )
            print("right_x2 (main):", right_x2)

            # x2x3
            var_a = self.x2
            var_a  = float(var_a)
            var_b = self.x3
            var_b = float(var_b)
            optimizer_var = 'x2x3'
            left_x1 = self.branch_bound( (var_a - 0.25) , var_b, Z, optimizer_var , 'left', 'var_a')
            right_x1 = self.branch_bound( (var_a + 0.25), var_b, Z, optimizer_var, 'right', 'var_a')
            left_x2 = self.branch_bound( var_a , (var_b - 0.25), Z, optimizer_var, 'left', 'var_b')
            right_x2 = self.branch_bound( var_a, (var_b+ 0.25), Z, optimizer_var, 'right', 'var_b')
            #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
            print()
            print( 'x2x3' )
            print("left_x1 (main) :" , left_x1 )
            print("right_x1 (main):", right_x1)
            print("left_x2 (main) :" , left_x2 )
            print("right_x2 (main):", right_x2)

            # x3x4
            var_a = self.x3
            var_a  = float(var_a)
            var_b = self.x4
            var_b = float(var_b)
            optimizer_var = 'x3x4'
            left_x1 = self.branch_bound( (var_a - 0.25) , var_b, Z, optimizer_var , 'left', 'var_a')
            right_x1 = self.branch_bound( (var_a + 0.25), var_b, Z, optimizer_var, 'right', 'var_a')
            left_x2 = self.branch_bound( var_a , (var_b - 0.25), Z, optimizer_var, 'left', 'var_b')
            right_x2 = self.branch_bound( var_a, (var_b+ 0.25), Z, optimizer_var, 'right', 'var_b')
            #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)
            print()
            print( 'x3x4' )
            print("left_x1 (main) :" , left_x1 )
            print("right_x1 (main):", right_x1)
            print("left_x2 (main) :" , left_x2 )
            print("right_x2 (main):", right_x2)

            # x4x5
            var_a = self.x4
            var_a  = float(var_a)
            var_b = self.x5
            var_b = float(var_b)
            optimizer_var = 'x4x5'
            left_x1 = self.branch_bound( (var_a - 0.25) , var_b, Z, optimizer_var , 'left', 'var_a')
            right_x1 = self.branch_bound( (var_a + 0.25), var_b, Z, optimizer_var, 'right', 'var_a')
            left_x2 = self.branch_bound( var_a , (var_b - 0.25), Z, optimizer_var, 'left', 'var_b')
            right_x2 = self.branch_bound( var_a, (var_b+ 0.25), Z, optimizer_var, 'right', 'var_b')
            #var1 = max(left_x1 ,right_x1 ,left_x2 ,right_x2)

            print()
            print( 'x4x5' )
            print("left_x1 (main) :" , left_x1 )
            print("right_x1 (main):", right_x1)
            print("left_x2 (main) :" , left_x2 )
            print("right_x2 (main):", right_x2)



    def objective_function(self,var_a,var_b, status):
        # ( 1 * x1 ) + ( 2 * x2 ) + ( 3 * x3 ) + ( 4 * x4 ) + ( 5 * x5 )
        if status == 'x1x2':    #x1x2
            Z = ( 1 * var_a ) + ( 2 * var_b ) + ( 3 * self.x3 ) + ( 4 * self.x4 ) + ( 5 * self.x5 )

        if status == 'x2x3':    #x2x3
            Z = ( 1 * self.x1 ) + ( 2 * var_a ) + ( 3 * var_b ) + ( 4 * self.x4 ) + ( 5 * self.x5 )

        if status == 'x3x4':    #x3x4
            Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * var_a ) + ( 4 * var_b ) + ( 5 * self.x5 )

        if status == 'x4x5':    #x4x5
            Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * self.x3 ) + ( 4 * var_a ) + ( 5 * var_b )

        if status == 'main':    #x4x5
            Z = ( 1 * self.x1 ) + ( 2 * self.x2 ) + ( 3 * self.x3 ) + ( 4 * self.x4 ) + ( 5 * self.x5 )
        return Z

    def constraint(self,var_a,var_b, status):
        constraint = 1500
        if status == 'x1x2':    #x1x2
            constraint = (5 * pow(var_a, 2)) + (45 * pow(var_b, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(self.x5, 2))
            # if constraint <= 1000:
            #     print("Constraint : ", constraint)

        if status == 'x2x3':    #x2x3
            constraint = (5 * pow(self.x1, 2)) + (45 * pow(var_a, 2)) + (3 * pow(var_b, 2)) + (2 * pow(self.x4, 2)) + (1 * pow(self.x5, 2))
            # if constraint <= 1000:
            #     print("Constraint : ", constraint)

        if status == 'x3x4':    #x3x4
            constraint = (5 * pow(self.x1, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(var_a, 2)) + (2 * pow(var_b, 2)) + (1 * pow(self.x5, 2))
            # if constraint <= 1000:
            #     print("Constraint : ", constraint)

        if status == 'x4x5':    #x4x5
            constraint = (5 * pow(self.x1, 2)) + (45 * pow(self.x2, 2)) + (3 * pow(self.x3, 2)) + (2 * pow(var_a, 2)) + (1 * pow(var_b, 2))
            # if constraint <= 1000:
            #     print("Constraint : ", constraint)

        if constraint <= 1000:
            return True
        return False

def main():
    m = matrx()
    m.run(m)

if __name__ == '__main__':
    main()

