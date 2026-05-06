# Classic Control¶

[ ![](/_static/videos/classic_control/acrobot.gif) Acrobot ](acrobot) [ ![](/_static/videos/classic_control/cart_pole.gif) Cart Pole ](cart_pole) [ ![](/_static/videos/classic_control/mountain_car_continuous.gif) Mountain Car Continuous ](mountain_car_continuous) [ ![](/_static/videos/classic_control/mountain_car.gif) Mountain Car ](mountain_car) [ ![](/_static/videos/classic_control/pendulum.gif) Pendulum ](pendulum)

The unique dependencies for this set of environments can be installed via:
    
    
    pip install gymnasium[classic-control]
    

There are five classic control environments: Acrobot, CartPole, Mountain Car, Continuous Mountain Car, and Pendulum. All of these environments are stochastic in terms of their initial state, within a given range. In addition, Acrobot has noise applied to the taken action. Also, regarding both mountain car environments, the cars are underpowered to climb the mountain, so it takes some effort to reach the top.

Among Gymnasium environments, this set of environments can be considered easier ones to solve by a policy.

All environments are highly configurable via arguments specified in each environment’s documentation.
