from math import sin, cos, pi
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class rwip:
    def __init__(self):
        # physics constants
        self.g = 9.80665  # N/m
        self.dt = 0.02  # seconds between state updates
        # physics model parameters
        self.m1 = 0.0224
        self.lc1 = 0.0192
        self.m2 = 0.340
        self.l1 = 0.040
        self.b1 = 62e-6
        self.b2 = 6.2e-6
        self.J1 = 16.1e-6
        self.Jc2 = 6.96e-6
        self.Kb = 0.0525
        self.Kt = 0.0525
        self.Ra = 2.07
        self.La = 0.00062
        # calculation intermediates
        self.gamma = (self.m1*self.lc1 + self.m2*self.l1)*self.g
        self.phi = 1/(self.J1 + self.m2*self.l1**2)
        self.zeta = 1/self.Jc2 + self.phi
        self.rho = self.Kb*self.Kt/self.Ra + self.b2
        self.nu = self.Kt/self.Ra



    def get_analog_action(self, action):
        # dummy, fixme
        return int(action)*0.5


    def simulate(self, action, state_tuple):
        """
        Simulate dynamics of the 1D RWIP

        Parameters
        ----------
        action : int
            [-2, 2]
        state_tuple : tuple
            State vector of theta_1, theta_1_dot, theta_2, theta_2_dot

        Returns
        -------
        new_state : tuple
            Updated state vector of theta_1, theta_1_dot, theta_2, theta_2_dot
        """
        theta_1, theta_1_dot, theta_2, theta_2_dot = state_tuple

        # analog action
        e_a = get_analog_action(action)

        # simulate physics through model
        theta_1_acc = self.gamma*self.phi*sin(theta_1) - self.b1*self.phi*theta_1_dot + self.phi*self.rho*theta_2_dot - self.nu*self.phi*e_a
        theta_2_acc = -self.gamma*self.phi*sin(theta_1) + self.b1*self.phi*theta_1_dot - self.rho*self.zeta*theta_2_dot + self.nu*self.zeta*e_a

        # state vars update
        new_theta_1 = theta_1 + theta_1_dot*self.dt
        new_theta_1_dot = theta_1_dot + theta_1_acc*self.dt
        new_theta_2 = theta_2 + theta_2_dot*self.dt
        new_theta_2_dot = theta_2_dot + theta_2_acc*self.dt
        new_state = (new_theta_1, new_theta_1_dot, new_theta_2, new_theta_2_dot)

        return new_state



    def discretize_state():
        #fixme
        pass

    def show_frame():
        #fixme
        pass



    

