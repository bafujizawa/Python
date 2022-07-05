class Scratch {
    public int Scratch(int n) {
        int num1 = 0;
        int num2 = 1;
        int counter = 0;
        
        while(counter <= n) {
            int num3 = num1 + num2;
            num1 = num2;
            num2 = num3;
            counter++;
        }
    return counter;
    }
}