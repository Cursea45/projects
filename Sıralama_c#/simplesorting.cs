using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SimpleSorting
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array = { 1, 45, 3, 23, 65, 21, 6 };
            selectionSort(array);
            Console.ReadKey();
        }
        static void selectionSort(int[] arr)
        {
            int min;
            int tur = 0;

            for (int i = 0; i < arr.Length - 1; i++)
            {
                min = i;
                for (int j = i + 1; j < arr.Length; j++)
                {
                    if (arr[j] < arr[min])
                    {
                        min = j;
                    }
                }
                int temp = arr[i];
                arr[i] = arr[min];
                arr[min] = temp;
                tur++;
                Console.Write("Tur " + tur + ": ");
                printArr(arr);
            }
        }
        static void printArr(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                Console.Write(arr[i] + " ");
            }
            Console.WriteLine();
        }
    }
}
