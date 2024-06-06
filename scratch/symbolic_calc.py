import sympy as s



# angular vel
w_h_x, w_h_y, w_h_z = s.symbols("w_h_x, w_h_y, w_h_z")
w_w_x, w_w_y, w_w_z = s.symbols("w_w_x, w_w_y, w_w_z")
w_h = s.Matrix([w_h_x, w_h_y, w_h_z])
w_w = s.Matrix([w_w_x, w_w_y, w_w_z])


# angular acc
alpha_h_x, alpha_h_y, alpha_h_z = s.symbols("alpha_h_x, alpha_h_y, alpha_h_z")
alpha_w_x, alpha_w_y, alpha_w_z = s.symbols("alpha_w_x, alpha_w_y, alpha_w_z")
alpha_h = s.Matrix([alpha_h_x, alpha_h_y, alpha_h_z])
alpha_w = s.Matrix([alpha_w_x, alpha_w_y, alpha_w_z])


# MoI
I_o_x, I_o_y, I_o_z = s.symbols("I_o_x, I_o_y, I_o_z")
I_w_x, I_w_y, I_w_z = s.symbols("I_w_x, I_w_y, I_w_z")
I_o = s.diag(I_o_x, I_o_y, I_o_z)
I_w = s.diag(I_w_x, I_w_y, I_w_z)


# Torque
T_x, T_y, T_z = s.symbols("T_x, T_y, T_z")
T = s.Matrix([T_x, T_y, T_z])

# m and g
m_x, m_y, m_z = s.symbols("m_x, m_y, m_z")
g_x, g_y, g_z = s.symbols("g_x, g_y, g_z")
m = s.Matrix([m_x, m_y, m_z])
g = s.Matrix([g_x, g_y, g_z])

# eq = I_o*alpha_h + I_w*alpha_w + w_h.cross(I_o*w_h + I_w*w_w) - m.cross(g)
# sol_x = s.solve(eq[0], alpha_h_x)

dt = s.symbols("dt")

print(g - dt*w_h.cross(g))

