
import numpy as np
import sympy as sym
import numdifftools as nd
import random

class matrx:
    detrm = 1
    Dimension = 3
    float_array = np.random.randn(Dimension, Dimension)
    a = 0

    inv_matrix = 0
    status = False

    v_1 = 0

    Av = 0
    sbv = 0
    norm = 0
    transpose_arr = 0

    vector = []
    vector_m = []
    row = 3
    col = 3
    minimizer = None
    # main method called in main to run
    def run(self, obj):


        Q = self.generate_Q()
        #Q.resize((self.row, 1))
        print("Q : " , Q)

        c = self.generate_c()
        #c.resize((3, 1))
        # print()
        print("c : ", c)


        print()
        matrix = self.gen_matrix( self.row, self.col) # generates random matrix

        # matrix = np.array( [[-0.92314982, - 0.26509944,  0.46311282],
        #     [0.79720349,  0.18733883,  0.37466323],
        #     [0.37234119, 0.53914955, - 0.12068839]]  )

        #this matrix gives second derivative as a convex function


        print("Matrix: " , matrix)
        print()
        self.minimizer = self.generate_some_minimizer_vicinity(matrix, 0 , self.col-1)
        print("minimizer : " , self.minimizer)

    #
        for i in range(0, len(matrix) ):
            col = matrix[:, [i]] # This is the vector of the matrix that will be passed
            print(col)
            b = self.apply_Function_problem_one(col, Q, c)
            b.resize((self.row, 1))
            d = self.find_convergence(b)
            #print("---")
            #print(d)
            #d = d.reshape((1, 3))

            print()
            print( " d: " ,d)
            print()
            #print( np.allclose(d, self.minimizer) )

    def generate_some_minimizer_vicinity(self, M, a, b):

        a = M[:, [a]]
        b = M[:, [b]]
        a_b = np.add(a,b)
        x_star = np.dot( (1/2) , a_b )
        #x_star = (1/2) * (a + b)
        return x_star


    def is_invertible(self, m):
        return m.shape[1] == m.shape[0] and np.linalg.matrix_rank(m) == m.shape[0]  # reference https://stackoverflow.com/questions/17931613/how-to-decide-a-whether-a-matrix-is-singular-in-python-numpy

    def apply_Function_problem_one(self, x,Q,c):
        #q_x = np.dot(Q,x)
        # print()
        # print("eeee")
        # print()

        q_x = Q * x

        #print("q_x : " , q_x)

        x_T_q_x = np.matmul( x.T, q_x)

        #print("x_T_q_x : ", q_x)

        one_two_x_T_q_x = np.dot( (1/2), x_T_q_x) #(1/2) * x_T_q_x

        #print("one_two_x_T_q_x : ", one_two_x_T_q_x)

        c_T_x = np.matmul( c.T, x) # c.T * x

        #print("c_T_x : ", one_two_x_T_q_x)

        e = np.add(one_two_x_T_q_x,c_T_x)

        #e.resize((self.row, 1))

        return e

    def find_convergence(self, F_x):
        der_One = np.gradient(F_x , axis=0)

        der_two = np.gradient(der_One,  axis=0)

        #print("gradient F''(x) = " , der_two)
        #print()


        # h = self.hessian(F_x)
        # a_step =  ( 1 /  h)
        #print("a_step : " , a_step )

        dt = -1 * der_One   # dt = - (gradient of Fxt)
        #print(" d_t :" , dt)

        # Formula

        # F(x_t+1) = F(x_t) +  a_t * [ gradient F(x_t)  ]^T * dt + ( 1/2 ) * a_t^2 * d_t^T * Hessian( x_t ) * d_t  + O( a_t^3 ||d_t||^3 ) )


        gradient_Ft_Transp_dt = np.matmul( der_One.T, dt ) # ---> [[ [ gradient F(x_t)  ]^T * dt ]]
        # NOTE :         # [ gradient F(x_t)  ]^T * dt < 0

        hess_dt = der_two * dt  # ---> [[ Hessian( x_t ) * d_t ]]
        # print("hess_dt : " , hess_dt)
        dt_trans_ = np.matmul( (dt.T), hess_dt) #---> [[ d_t^T ]] * [[ Hessian( x_t ) * d_t ]]
        # dt_trans_ = (dt.T) * hess_dt


        a_step_a = gradient_Ft_Transp_dt# [gradient F(x_t)] ^ T * dt
        a_step_b = dt_trans_ * dt
        #a_step_b = np.matmul( dt_trans_ , dt)
        a_step = (-2) * (a_step_a / a_step_b)   # 0< at < -2 [grad Fx]^T dt/ dT Hxt dt


        #[a_t * [gradient F(x_t)] ^ T * dt] - < 0
        at_MULT_gradient_Ft_Transp_dt = np.matmul(a_step, gradient_Ft_Transp_dt) # ---> [[ a_t ]] * [[ [ gradient F(x_t)  ]^T * dt ]]
        print("ss :" , at_MULT_gradient_Ft_Transp_dt)

        #[(1 / 2) *  [ [ [ [a_t ^ 2] * d_t ^ T] * Hessian(x_t)]  * d_t] ]
        a_t_step_square = pow(a_step, 2)
        a_t_sq_MULT_dt_trans_ = np.matmul(a_t_step_square , dt_trans_)
        #a_t_sq_MULT_dt_trans_MULT_hess = np.matmul( a_t_sq_MULT_dt_trans_, hess_dt)
        a_t_sq_MULT_dt_trans_MULT_hess = a_t_sq_MULT_dt_trans_ *  hess_dt
        #a_t_sq_MULT_dt_trans_MULT_hess_MULT_dt =  np.matmul(a_t_sq_MULT_dt_trans_MULT_hess, dt)
        a_t_sq_MULT_dt_trans_MULT_hess_MULT_dt = a_t_sq_MULT_dt_trans_MULT_hess * dt
        one_two_a_t_sq_dt_trans_ = np.dot((1 / 2), a_t_sq_MULT_dt_trans_MULT_hess_MULT_dt)

        #O(a_t ^ 3 | | d_t | | ^ 3 ) )

        a_three = pow(a_step , 3)
        d_three = a_three = np.linalg.norm(dt)
        d_three = pow(d_three, 3)

        ad = a_three * d_three
        #ad = np.matmul(a_three * d_three)

        z = F_x + at_MULT_gradient_Ft_Transp_dt + one_two_a_t_sq_dt_trans_ + ad
        return z
        #
        # F(x_t+1) = F(x_t)  +   a_t * [ gradient F(x_t)  ]^T * dt   +
        # ( 1/2 ) * a_t^2 * d_t^T * Hessian( x_t ) * d_t + O( a_t^3 ||d_t||^3 ) )

        # dt = - ( gradient F(x_t) )
        # or
        # dt = -H(x_t)^-1 [ gradient F(x_t) ]


    # https://stackoverflow.com/questions/31206443/numpy-second-derivative-of-a-ndimensional-array
    def hessian(self, x):
        """
        Calculate the hessian matrix with finite differences
        Parameters:
           - x : ndarray
        Returns:
           an array of shape (x.dim, x.ndim) + x.shape
           where the array[i, j, ...] corresponds to the second derivative x_ij
        """
        print( " x x x x " )
        x_grad = np.gradient(x, axis= 0)
        hessian = np.empty((x.ndim, x.ndim) + x.shape, dtype=x.dtype)
        print(hessian)
        for k, grad_k in enumerate(x_grad):
            # iterate over dimensions
            # apply gradient again to every component of the first derivative.
            tmp_grad = np.gradient(grad_k.T[0])
            print(tmp_grad)
            for l, grad_kl in enumerate(tmp_grad):
                hessian[k, l, :, :] = grad_kl
        return hessian


    def generate_c(self):
        c = np.random.randn(self.row, 1)######## CHANGING DIMENSION OF ARRAY
        return c

    # Generate Q - Its a symmetric positive definite matrix
    def generate_Q(self):
        # Q is a symmetric, positive definite function, and c is a real vector
        matrix = self.gen_sym_matrix_positive_definite()
        return matrix

    def gen_sym_matrix_positive_definite(self):
        a = False
        while a == False:
            matrix = np.random.randn(self.row, 1)  ######## CHANGING DIMENSION OF ARRAY
            symmetric_matrix = np.matmul(matrix, matrix.T)
            a = self.is_positive_definite(symmetric_matrix)
            if a == True:
                break
        if a== True:
            return symmetric_matrix

    def is_positive_definite(self,x):
        return np.all(np.linalg.eigvals(x) > 0)

    # condition that is true when you have a matrix that is invertible
    def gen_matrix(self, d_row, d_col):

        float_array = np.random.randn(d_row, d_col)
        #self.a = float_array.astype(float)
        check = False
        c = False
        while check!= True:
            check = self.is_invertible(float_array)
            if check == True:
                a = float_array.astype(float)  # convert float matrix into int matrix
                float_array = np.linalg.inv(a)
                c = True
                break
            else:
                float_array = np.random.randn(d_row, d_col)

        if c == True:
            return float_array


    def get_inv_matrix(self):
        inv_matrix = np.linalg.inv(self.a)
        return inv_matrix














    def get_matrix(self):
        return self.a


    def part_one(self):
        k=0
        inv = self.get_inv_matrix()
        v_1 = inv[:, [k]]


        print("matrix")
        print(self.a)
        print("invs of matrix")
        print(self.inv_matrix)

        #To get Av = Array * Vector of kth column of inverse matrix
        orignal_matrix = self.get_matrix()
        Av = np.matmul(orignal_matrix , v_1)    # A * V
        self.Av = Av

        sbv = np.zeros(3)   # Standard vector basis = ek -> ek is the svb of the vk
        sbv[k] = 1
        sbv = sbv.reshape((3, 1))
        self.sbv = sbv

        av_sbv_norm = np.linalg.norm( Av-sbv, axis=1 )  #    ||Av-ek|| l2 norm

        print()
        print("Part One - We want to find an v that satisfies Av = ek, or that minimizes")

        status = np.allclose(self.Av, self.sbv) # Using numpys.allClose to compare two float arrays - if equal proceeds to step 2
        if status == True:
            print("Av=ek - Satisfies (using np.allClose to compare the two vectors)")
            print("Av=ek")
            print(Av)
            print(sbv)
            return True

        sbv_zero = np.zeros(self.Dimension)
        status = np.allclose(av_sbv_norm, sbv_zero)
        if status == True:
            print("|Av-ek|2 norm - Satisfies")
            return True

        return False

    def part_two(self):
        norm_Av_sub_svb = np.subtract(self.Av,self.sbv)
        self.norm = np.linalg.norm(norm_Av_sub_svb, axis=1) # ||Av-ek||
        self.norm = self.norm.reshape((3, 1))
        det_norm = self.norm

        #det_norm = np.gradient(det_norm, axis=0)
        #det_norm= det_norm.reshape((3, 1))
        gradient_norm = det_norm.astype(int)    # dn2 is int

        self.transpose_arr = np.copy(self.a)
        self.transpose_arr = self.transpose_arr.transpose()

        AT_Av = np.matmul (self.transpose_arr, self.Av) # A transpose * A * V
        AT_ek = np.matmul (self.transpose_arr, self.sbv)# A transpose * Ek
        AtAv_ATek = np.subtract(AT_Av, AT_ek)
        det_AtAv_ATek = np.gradient(AtAv_ATek, axis=0)  # taking deri of nrom   # Gradient of ATAv − ATek
        #det_AtAv_ATek= det_AtAv_ATek.reshape((3, 1))


        print()
        print(" Show that the gradient of ||Av − ek|| is given by ATAv − ATek")
        status = np.allclose(det_norm, det_AtAv_ATek) # Using numpys.allClose to compare two float arrays - if equal proceeds to step 2
        if status == True:
            print(" Part 2 satisfies")


    # To calc gradient of ( AT*Av-AT*Ek )
    # Im using this for Part 4 in in part 3
    def grad_norm(self,v):
        Ek = self.sbv
        vectr = v
        A_T = self.transpose_arr
        orig_a = self.a
        Av_mult_vect = np.matmul( orig_a , vectr)
        AT_x_Av_mult_vect = np.matmul( A_T , Av_mult_vect)  # AT*Av
        A_T_mult_Ek = np.matmul( A_T , Ek)  # AT*Ek
        av_sub_ek = np.subtract(AT_x_Av_mult_vect, A_T_mult_Ek) #AT*Av-AT*Ek
        dx_norm = np.gradient(av_sub_ek, axis=0)
        #dx_norm= dx_norm.reshape((3, 1))
        return dx_norm

    # Returns the very first feature to compute other feature values
    def first_v_feature(self, a):
        d_dim_vector = np.random.randn(self.Dimension, 1)       # Pass here the required col vector
        #d_dim_vector = self.a[:, [1]]  # I was taking v0 as first col of matrix
        alpha = a
        old_v = alpha * self.grad_norm(d_dim_vector)
        return old_v

    def part_three(self, feature, alph):
        print("Part 3 & 4")
        print("Verify for a few dimensions D, for a few experimental A; k each, and good choices of step size α that this process does converge to the desired solution")


        v_feature = self.a[:, [feature]]       # Pass here the required col vector
        #d_dim_vector = self.a[:, [1]]  # I was taking v0 as first col of matrix
        first_v_feature_for_test = self.first_v_feature(alph)
        alpha = alph
        v_prev = np.subtract(v_feature, (first_v_feature_for_test * first_v_feature_for_test))

        t = 1
        while t<3:
            aX = alpha * self.grad_norm(v_prev)
            new_v = v_prev - aX
            say = new_v.reshape((1, 3))
            print("==============")
            print("calculation:")
            print(say)    # this is v1 and im comparing it to orignal v1 and seeing the difference
            print("Given :")
            print(self.a[: ,[feature]])
            print("==============")
            print("Part four")
            print("Error decay")
            print(self.part_four(new_v))
            print()

            v_prev = new_v
            t += 1

    def part_six(self , feature, alph):
        print()
        print("Part 6")
        print(" Instead of proceeding by fixed step size α, consider a variable stepsize αt. Find an expression for theoptimal stepsize to take at time t in terms of A, vt, e")


        v_feature = self.a[:, [feature]]       # Pass here the required col vector
        first_v_feature_for_test = self.first_v_feature(alph)
        alpha = alph
        v_prev = np.subtract(v_feature, (first_v_feature_for_test * first_v_feature_for_test))
        print()


        t = 1
        while t<5:
            aX = alpha * self.grad_norm(v_prev)
            new_v = v_prev - aX
            say = new_v.reshape((1, 3))
            print("==============")
            print("calculation:")
            print(say)    # this is v1 and im comparing it to orignal v1 and seeing the difference
            print("From given matric :")
            print(self.a[: ,[feature]])
            print("==============")
            print("Part four")
            print("Error decay")
            print(self.part_four(new_v))
            print()

            v_prev = new_v
            alpha = alpha + np.square(alpha)
            t += 1

    def part_four(self,v):
        Ek = self.sbv
        orig_a = self.a
        vect = v
        A_V = np.matmul(orig_a,vect)
        AVt_subtract_Ek = np.subtract(A_V,Ek)
        AVt_subtract_Ek_norm = np.linalg.norm( AVt_subtract_Ek, axis=1)
        return AVt_subtract_Ek_norm

def main():
    m = matrx()
    m.run(m)

if __name__ == '__main__':
    main()

