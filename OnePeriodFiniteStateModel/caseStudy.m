clear all
close all

%-----------------------------
% 2D Case
%   -3 Securities
%   -2 States
%-----------------------------

origin = [0 0];
bond = [1 1];
stock = [2 1];
option = [3 4];



figure
arrow(origin, bond, 'EdgeColor', 'b', 'FaceColor', 'b')
hold on 
arrow(origin, stock, 'EdgeColor', 'r', 'FaceColor', 'r')
hold on
arrow(origin, option);
legend('Bond', 'Stock', 'Option','Location', 'NorthWest')

A = [bond' stock']

x = inv(A)*option';

bond = bond.*x(1);
stock = stock.*x(2);
hedge = bond+stock;

figure
arrow(origin, bond, 'EdgeColor', 'b', 'FaceColor', 'b')
hold on
arrow(bond, bond+stock, 'EdgeColor', 'r', 'FaceColor', 'r');
hold on
arrow(origin, hedge);
legend('Bond', 'Stock', 'Option','Location', 'NorthWest')

%-----------------------------
% ND Case
%   -N Securities
%   -M States
%-----------------------------

securities = [];

bond_1 = [1 1 4 9 3];
bond_2 = [1 1 4 9 3];
bond_3 = [-2 1 -6 7 -3];
stock_4 = [-0.2 0.1 -0.6 0.7 -0.3];
stock_5 = [-0.69 0.71 -0.705 0.703 0.68];
stock_6 = [2 2.1 2.3 1.99 2.02];
option_7 = [0.1 -0.1 0.4 0.9 -0.3];
option_8 = [-6.9 7.1 -7.05 7.03 6.8];

pMatrix = [bond_1' bond_2' bond_3' stock_4' stock_5'...
    stock_6' option_7' option_8']

AD = rref(pMatrix)
A = [];
basis = [];
pivot = 1;
for j=1:length(AD(1,:))
    if (pivot <= length(AD(:,1)) && AD(pivot, j) == 1)
        pMatrix(:,j)
        A = [A pMatrix(:,j)];
        pivot = pivot + 1;
        basis = [basis j];
    end
        
end
A
asset_1 = [4 3 -4 8 -6];
asset_2 = [4.5 3.5 3.7 -4 -3];
asset_3 = [-3.0 -4.5 3.4 2.9 2]; 
asset_4 = [-2 1 -6 7 -3];

assets = [asset_1' asset_2' asset_3' asset_4']

x = inv(A)*assets


