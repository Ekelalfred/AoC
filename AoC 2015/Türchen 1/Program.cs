class Türchen1
{
    public static char[] zeichen;

    public static void Main(String[] args)
    {
        StreamReader sr = new StreamReader("../../../input.txt");
        zeichen = sr.ReadToEnd().ToCharArray();
        RechneStockwerk();
        WannKeller();
    }

    public static void RechneStockwerk()
    {
        int stockwerk = 0;
        for (int i = 0; i < zeichen.Length; i++)
        {
            if (zeichen[i].ToString().Equals("("))
            {
                stockwerk++;
            }
            else
            {
                stockwerk--;
            }
        }
        Console.WriteLine("Wir befinden uns in Stockwerk: " + stockwerk);
    }

    public static void WannKeller()
    {
        int stockwerk = 0;
        for (int i = 0; i <= zeichen.Length; i++)
        {
            if (zeichen[i].ToString().Equals("("))
            {
                stockwerk++;
            }
            else
            {
                stockwerk--;
            }
            if (stockwerk < 0)
            {
                Console.WriteLine("Bei Instruktion " + (i + 1) + " gehen wir in den Keller.");
                return;
            }
        }
    }
}