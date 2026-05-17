module x (
    input [3:0] d0,
    input [3:0] d1,
    input s,
    output [3:0] y
);
    assign y = s?d0:d1;
endmodule