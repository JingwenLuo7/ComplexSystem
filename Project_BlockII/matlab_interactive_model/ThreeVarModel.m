function sys = ThreeVarModel()
    % Define parameters
    sys.pardef = [ 
        struct('name','a',  'value',0.1);
        struct('name','b',  'value',0.1);
        struct('name','K',  'value',0.2);
        struct('name','V1', 'value',1.0);
        struct('name','V2', 'value',1.5);
        struct('name','K1', 'value',0.01);
        struct('name','K2', 'value',0.01);
        struct('name','V3', 'value',6.0);
        struct('name','V4', 'value',2.5);
        struct('name','K3', 'value',0.01);
        struct('name','K4', 'value',0.01)
    ];

    % Define variables (initial conditions)
    sys.vardef = [ 
        struct('name','P', 'value',0.5);
        struct('name','Q', 'value',0.5);
        struct('name','R', 'value',0.5)
    ];

    % Define ODE function
    sys.odefun = @odefun;

    % Time span
    sys.tspan = [0 100];

    % LaTeX for panel
    sys.panels.bdLatexPanel.title = '3-Variable Model';
    sys.panels.bdLatexPanel.latex = {
        '\textbf{Three-variable system}', ...
        'Equations:', ...
        '$\dot{P} = a Q - \frac{b P}{K + P}$', ...
        '$\dot{Q} = V_1 \frac{1 - Q}{K_1 + (1 - Q)} - V_2 R \frac{Q}{K_2 + Q}$', ...
        '$\dot{R} = P V_3 \frac{1 - R}{K_3 + (1 - R)} - V_4 \frac{R}{K_4 + R}$'
};

end

% ODE function required by bdtoolbox
function dY = odefun(t,Y,a,b,K,V1,V2,K1,K2,V3,V4,K3,K4)
    P = Y(1);
    Q = Y(2);
    R = Y(3);

    dP = a*Q - b*P/(K + P);
    dQ = V1*(1-Q)/(K1 + (1-Q)) - V2*R*Q/(K2 + Q);
    dR = P*V3*(1-R)/(K3 + (1-R)) - V4*R/(K4 + R);

    dY = [dP; dQ; dR];
end
