import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class rwip:
    def __init__(self):
        # physics constants
        self.g = 9.80665  # N/m
        self.dt = 0.02  # seconds between state updates
        # physics model parameters
        self.K_t = np.array([0.0525, 0.0525, 0.0525])
        self.K_b = np.array([0.0525, 0.0525, 0.0525])
        self.R_a = np.array([2.07, 2.07, 2.07])
        self.I_w = 15e-6
        self.I_c = 5e-6
        self.I_o = self.I_c + self.I_w
        self.m_vec = 1*np.array([0.08, 0.08, 0.08])  # total mass center of gravity

        # calculation intermediates
        self.precomp_1 = 1/(self.I_o - self.I_w)



    def get_analog_action(self, action):
        # fixme
        return np.array([0, 0, 0])


    def simulate(self, action, state_tuple):
        """
        Simulate dynamics of the 3D RWIP for delta time

        Parameters
        ----------
        action : int
            Actions
        state_tuple : tuple
            State vector

        Returns
        -------
        new_state : tuple
            Updated state vector
        """
        theta_c, theta_c_dot, theta_w, theta_w_dot, g = state_tuple

        # Dynamics described with body fixed coordinate frame

        # intermediate calc
        e_a = get_analog_action(action)
        T = self.K_t/self.R_a*(e_a - self.K_b*theta_c_dot)
        precomp_A = np.cross(theta_c_dot, (self.I_o*theta_c_dot + self.I_w*theta_w_dot))
        precomp_B = np.cross(self.m_vec, g)

        # simulate physics through model
        theta_c_acc = self.precomp_1*(-precomp_A - T + precomp_B)
        theta_w_acc = self.precomp_1*(precomp_A + self.I_o/self.I_w*T - precomp_B)

        # state vars update
        new_theta_c = theta_c + theta_c_dot*self.dt
        new_theta_c_dot = theta_c_dot + theta_c_acc*self.dt
        new_theta_w = theta_w + theta_w_dot*self.dt
        new_theta_w_dot = theta_w_dot + theta_w_acc*self.dt
        new_g = g + self.dt*np.cross(-w_h, g)
        new_state = (new_theta_c, new_theta_c_dot, new_theta_w, new_theta_w_dot, new_g)

        return new_state



    def discretize_state():
        #fixme
        pass

    def show_frame():
        #fixme
        pass



    

