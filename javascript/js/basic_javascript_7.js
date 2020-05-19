var x = 1;

function Add1() {
    document.write(1 + x + '<br>');
}
function Add2() {
    document.write(2 + x + '<br>');
}
function Add3() {
    var y = 2;
    document.write(3 + y + '<br>');
}
function Add4() {
    console.log(4 + y);
}

Add1();
Add2();
Add3();
Add4();