using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DSProje2
{

    class Musteri
    {
        public String MüşteriAdı;
        public int ÜrünSayısı;
        public static int nesneSayısı;
        public Musteri(String MüşteriAdı,int ÜrünSayısı)
        {
            this.MüşteriAdı = MüşteriAdı;
            this.ÜrünSayısı = ÜrünSayısı;
            nesneSayısı++;
        }
        

    }
    class ÖncelikliKuyruk
    {
        public List<Musteri> liste;
        public int nesneSayisi;
        public ÖncelikliKuyruk()
        {
            liste = new List<Musteri>();
            nesneSayisi++;
        }
        public void ekle(Musteri o)
        {
            liste.Add(o);
        }
        public int sil()
        {
            Musteri min = liste.ElementAt(0);
            int minIndex = 0;
            int minUrunSayisi = 0;

            for (int i = 1; i < liste.Count; i++)
            {
                if (liste.ElementAt(i).ÜrünSayısı < min.ÜrünSayısı)
                {
                    min = liste.ElementAt(i);
                    minIndex = i;
                }
            }
            Console.WriteLine("En düşük ürün sayısına sahip eleman silindi: " + liste.ElementAt(minIndex).MüşteriAdı + ", " + liste.ElementAt(minIndex).ÜrünSayısı);
            minUrunSayisi = liste.ElementAt(minIndex).ÜrünSayısı;
            liste.RemoveAt(minIndex);
            return minUrunSayisi;

        }

        public Boolean bosMu()
        {
            return (liste.Count == 0);
        }

    }

    class Queue
    {
        public int maxSize;
        public Musteri[] queArray;
        public int front;
        public int rear;
        public int nItems;
        public Queue(int size)
        {
            maxSize = size;
            queArray = new Musteri[maxSize];
            front = 0;
            rear = -1;
            nItems = 0;
        }
        public void insert(Musteri o)
        {
            if(rear == maxSize - 1)
            {
                rear = -1;
            }
            queArray[++rear] = o;
            nItems++;
        }
        public object remove()
        {
            object temp = queArray[front++];
            if (front == maxSize)
            {
                front = 0;
            }
            nItems--;
            return temp;
        }
        public object peekFront()
        {
            return queArray[front];
        }
        public Boolean isEmpty()
        {
            return (nItems == 0);
        }
        public Boolean isFull()
        {
            return (nItems == maxSize);
        }
        public int size()
        {
            return nItems;
        }
        

    }
    class Stack
    {

        public int maxSize;
        public Musteri[] stackArray;
        public int top;
        public Stack(int size)
        {
            maxSize = size;
            stackArray = new Musteri[maxSize];
            top = -1;
        }

        public void push(Musteri newItem)
        {
            stackArray[++top] = newItem;
        }
        public object pop()
        {
            return stackArray[top--];
        }
        public object peek()
        {
            return stackArray[top];
        }
        public Boolean isEmpty()
        {
            return (top == -1);
        }
        public Boolean isFull()
        {
            return (top == maxSize - 1);
        }
        
    }
    class Program
    {
        static void Main(string[] args)
        {
            Random rastgele = new Random();
            String[] MüşteriAdı = { "Ali", "Merve", "Veli", "Gülay", "Okan", "Zekiye", "Kemal", "Banu", "İlker", "Songül", "Nuri", "Deniz" };
            int[] ÜrünSayısı = { 8, 11, 16, 5, 15, 14, 19, 3, 18, 17, 13, 15 };
            ArrayList Arrayliste = new ArrayList();
            int sayac = 0;
            int sayac2 = 0;
            Musteri musteri;
            List<Musteri> genericListe;

            while (sayac < MüşteriAdı.Length)
            {
                genericListe = new List<Musteri>();
                int genericListeLenght = rastgele.Next(1,5);
                for(int i = 0; i < genericListeLenght; i++)
                {
                    musteri = new Musteri(MüşteriAdı[sayac], ÜrünSayısı[sayac]);
                    genericListe.Add(musteri);
                    sayac++;
                    if (sayac == MüşteriAdı.Length)
                        break;
                }
                Arrayliste.Add(genericListe);
                sayac2++;
                
            }
            foreach(List<Musteri>item in Arrayliste)
            {
                foreach(Musteri item1 in item)
                {
                    Console.WriteLine("{0}, {1}", item1.MüşteriAdı, item1.ÜrünSayısı);
                }
                Console.WriteLine();
            }
            Console.WriteLine("Arraylistteki eleman sayısı:{0}", sayac2);
            Console.WriteLine("Listelerin ortalama eleman sayısı: {0}", ((double)Musteri.nesneSayısı / (double)sayac2));
            
            

            

            Console.WriteLine("******************YIĞIT******************");
            Stack stack = new Stack(MüşteriAdı.Length);

            for(int i = 0; i < MüşteriAdı.Length; i++)
            {
                stack.push(new Musteri(MüşteriAdı[i], ÜrünSayısı[i]));

                
            }
                


            while (!stack.isEmpty())
            {
                Musteri value = (Musteri)stack.pop();
                Console.WriteLine(value.MüşteriAdı+", "+value.ÜrünSayısı);
                
            }

            Console.WriteLine("******************KUYRUK******************");
            
            Queue queue = new Queue(MüşteriAdı.Length);
            for (int i = 0; i < MüşteriAdı.Length; i++)
            {
                musteri = new Musteri(MüşteriAdı[i], ÜrünSayısı[i]);
                queue.insert(musteri);
            }
            while (!queue.isEmpty())
            {
                Musteri value = (Musteri)queue.remove();
                Console.WriteLine(value.MüşteriAdı+","+value.ÜrünSayısı);
            }
            

            ÖncelikliKuyruk PQ = new ÖncelikliKuyruk();
            for (int i = 0; i < MüşteriAdı.Length; i++)
            {
                PQ.ekle(new Musteri(MüşteriAdı[i], ÜrünSayısı[i]));
            }
            while (!PQ.bosMu())
            {
                PQ.sil();
            }

            Console.WriteLine("************************");
            Console.WriteLine("İŞLEM TAMAMLAMA SÜRELERİ");
            Console.WriteLine("************************");
            for (int i = 0; i < MüşteriAdı.Length; i++)
            {
                musteri = new Musteri(MüşteriAdı[i], ÜrünSayısı[i]);
                queue.insert(musteri);
                
            }
            int queue_ortalama_sure=0;
            while (!(queue.size()==0))
            {
                Musteri value = (Musteri)queue.remove();
                Console.WriteLine("Güle güle sayın "+value.MüşteriAdı+" "+value.ÜrünSayısı+" dakika işlem süresiyle aramızdan ayrıldı.");
                queue_ortalama_sure += value.ÜrünSayısı / (queue.size()+1);
            }
            Console.WriteLine("QUEUE İLE ORTALAMA İŞLEM SÜRESİ:" + queue_ortalama_sure+" DK");
            for (int i = 0; i < MüşteriAdı.Length; i++)
            {
                PQ.ekle(new Musteri(MüşteriAdı[i], ÜrünSayısı[i]));
            }
            int PQ_ort_sure=0;
            while (!PQ.bosMu())
            {
                PQ_ort_sure += PQ.sil()/(PQ.liste.Count+1);
            }
            Console.WriteLine("ÖNCELİKLİ SIRA İLE ORTALAMA İŞLEM SÜRESİ:" + PQ_ort_sure+" DK");
            Console.ReadLine();





        }
    }
}
