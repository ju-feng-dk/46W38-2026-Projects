import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.integrate import solve_ivp

ct_curve = np.loadtxt('turbie_inputs/CT.txt')

def get_ct(ws):
    return np.interp(ws, ct_curve[:, 0], ct_curve[:, 1],
                     left=0, right=0)

mb = 41e3     # mb [kg]
mn = 446e3    # mn [kg]
mh = 105e3    # mh [kg]
mt = 628e3    # mt [kg]
c1 = 4.208e3  # c1 [N/(m/s)]
c2 = 1.273e4  # c2 [N/(m/s)]
k1 = 1.711e6  # k1 [N/(m/s)^2]
k2 = 3.278e6  # k2 [N/(m/s)^2]

m1 = mb*3
m2 = mn + mh + mt

M = np.array([[m1, 0],
              [0, m2]])
C = np.array([[c1, -c1],
              [-c1, c1 + c2]])
K = np.array([[k1, -k1],
              [-k1, k1 + k2]])
D = 178   # Dr [m]
rho = 1.22  # rho [kg/m3]
A = np.pi * (D/2)**2  # A [m2]

def load_wind_data(filename):
    data = np.loadtxt(filename, skiprows=1)
    return data

wind_data = load_wind_data(
    'wind_files/wind_TI_0.1/wind_12_ms_TI_0.1.txt')

avg_wind_speed = 12.0  # m/s

def get_wind_speed(t):
    return np.interp(t, wind_data[:, 0], wind_data[:, 1])

def cal_aero_force(t, x1dot):
    ws = get_wind_speed(t)
    ct = get_ct(avg_wind_speed)
    F_aero = 0.5 * rho * A * ct * (ws - x1dot)*np.abs(ws - x1dot)
    return F_aero

A_array = np.zeros((4, 4))
A_array[:2, :2] = np.zeros((2, 2))
A_array[:2, 2:] = np.eye(2)
A_array[2:, :2] = -np.linalg.inv(M) @ K
A_array[2:, 2:] = -np.linalg.inv(M) @ C

B_array = np.zeros((4, 4))
B_array[2:, 2:] = np.linalg.inv(M)

M_inv = np.linalg.inv(M)
MK = M_inv @ K
MC = M_inv @ C

def dydt(t, y): 
    x1, x2, x1dot, x2dot = y

    F_aero = cal_aero_force(t, x1dot)
    #F_aero = 0
    
    res = np.zeros(4)
    res[0] = x1dot
    res[1] = x2dot



    res[2] = -MK[0, 0]*x1 - MK[0, 1]*x2 - MC[0, 0]*x1dot - MC[0, 1]*x2dot + M_inv[0, 0]*F_aero
    res[3] = -MK[1, 0]*x1 - MK[1, 1]*x2 - MC[1, 0]*x1dot - MC[1, 1]*x2dot + M_inv[1, 0]*F_aero
    return res

def dydt_matrix(t, y): 
    x1, x2, x1dot, x2dot = y

    F_aero = cal_aero_force(t, x1dot)
    #F_aero = 0
    
    res = A_array @ y + B_array @ np.array([0, 0, F_aero, 0])
    return res

y0 = [0, 0, 0, 0]  # Initial conditions: [x1, x2, x1dot, x2dot]
t_span = (0, 660)   # Time span for the simulation

t0, tf, dt = 0, 660, 0.01

# inputs to solve ivp
tspan = [t0, tf]   # 2-element list of start, stop
y0 = [0, 0, 0, 0]  # initial condition
t_eval = np.arange(t0, tf, dt)  # times at which we want output

for avg_wind_speed in np.arange(4, 26):
    wind_data = load_wind_data(
        f'wind_files/wind_TI_0.15/wind_{avg_wind_speed}_ms_TI_0.15.txt')
    

    s = time.time()
    sol = solve_ivp(dydt, t_span, y0, t_eval=t_eval) #, t_eval=np.linspace(t_span[0], t_span[-1], 6001))
    e = time.time()
    print(f'Simulation time: {e - s:.2f} seconds')
    print(f'Wind Speed: {avg_wind_speed} m/s')
    print(f'mean x1: {np.mean(sol.y[0, :]):.4f} m, mean x2: {np.mean(sol.y[1, :]):.4f} m\n')

    fig = plt.subplots(3, 1, figsize=(10, 12))
    plt.suptitle(f'Avg Wind Speed: {avg_wind_speed} m/s', fontsize=16)
    plt.subplot(3, 1, 1)
    plt.plot(sol.t, sol.y[0, :], label='x1')
    #plt.xlabel('Time [s]')
    plt.ylabel('Displacement x1 [m]')
    #plt.title('Tower Top Displacement Over Time')
    plt.legend()    
    plt.grid()
    plt.subplot(3, 1, 2)
    plt.plot(sol.t, sol.y[1, :], label='x2', color='orange')
    #plt.xlabel('Time [s]')
    plt.ylabel('Displacement x2 [m]')
    #plt.title('Nacelle Displacement Over Time')
    plt.legend()
    plt.grid()
    plt.subplot(3, 1, 3)
    plt.plot(sol.t, get_wind_speed(sol.t), label='Wind Speed', color='green')
    plt.xlabel('Time [s]')
    plt.ylabel('Wind Speed [m/s]')
    #plt.title('Wind Speed Over Time')
    plt.legend()
    plt.grid()
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f'outputs/WT_response_WS_{avg_wind_speed}_ms.png')
    plt.close()









