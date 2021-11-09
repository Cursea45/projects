using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DSProje3
{
    // Düğüm Sınıfı
    class TreeNode
    {
        public Duraklar data;
        public TreeNode leftChild;
        public TreeNode rightChild;
        public void displayNode()
        {
            Console.Write("Durak Adı:" + data.DurakAdi + "\nBP:" + data.BosPark + "\nTB:" + data.TandemSayisi + "\nNB:" + data.NormalSayisi + "\nDuraktan bisiklet kiralayan müşteri sayısı:" + data.kiralayan_müşteri_sayısı + "\nMüşteri Listesi: \n\n");
            data.müşterileri_yazdir(data.müşteriler);
            Console.WriteLine("");
        }
    }

    // Agaç Sınıfı
    class Tree
    {
        private TreeNode root;
        public int sayi;

        public Tree() { root = null; }

        public int totalDepth;
        public int maxDepth;
        public TreeNode getRoot()
        { return root; }

        // Agacın preOrder Dolasılması
        public void preOrder(TreeNode localRoot)
        {
            if (localRoot != null)
            {
                localRoot.displayNode();
                preOrder(localRoot.leftChild);
                preOrder(localRoot.rightChild);
            }
        }

        // Agacın inOrder Dolasılması
        public void inOrder(TreeNode localRoot)
        {
            if (localRoot != null)
            {
                inOrder(localRoot.leftChild);
                localRoot.displayNode();
                inOrder(localRoot.rightChild);
            }
        }

        // Agacın postOrder Dolasılması
        public void postOrder(TreeNode localRoot)
        {
            if (localRoot != null)
            {
                postOrder(localRoot.leftChild);
                postOrder(localRoot.rightChild);
                localRoot.displayNode();
            }
        }

        // Agaca bir dügüm eklemeyi saglayan metot
        public void insert(Duraklar newdata)
        {
            TreeNode newNode = new TreeNode();
            newNode.data = newdata;
            if (root == null)
                root = newNode;
            else
            {
                TreeNode current = root;
                TreeNode parent;
                while (true)
                {
                    parent = current;
                    if (string.Compare(newdata.DurakAdi, current.data.DurakAdi) == -1)
                    {
                        current = current.leftChild;
                        if (current == null)
                        {
                            parent.leftChild = newNode;
                            return;
                        }
                    }
                    else
                    {
                        current = current.rightChild;
                        if (current == null)
                        {
                            parent.rightChild = newNode;
                            return;
                        }
                    }
                } // end while
            } // end else not root
        } // end insert()
        private void traverseTreeForInfo(TreeNode node, int depth)
        {
            if (node != null)
            {
                depth++;


                if (depth > maxDepth)
                    maxDepth = depth; //update max depth

                totalDepth += depth;


                traverseTreeForInfo(node.leftChild, depth); //traverse left sub-tree
                traverseTreeForInfo(node.rightChild, depth); //traverse right sub-tree

            }
        }
        public void derinlikBul(TreeNode rootNode, int treeSize)
        {

            totalDepth = 0;
            maxDepth = 0;


            traverseTreeForInfo(rootNode, -1);

            Console.WriteLine("\nAğacın Derinliği: " + maxDepth);

        } // class Tree
        public void musteriBul(int ID, TreeNode localRoot)
        {
            if (localRoot != null)
            {

                musteriBul(ID, localRoot.leftChild);
                for (int i = 0; i < localRoot.data.müşteriler.Count; i++)
                {
                    if (localRoot.data.müşteriler.ElementAt(i).ID == ID)
                    {
                        System.Console.WriteLine(localRoot.data.müşteriler.ElementAt(i).kiralama_saati + " saatinde " + localRoot.data.DurakAdi + " durağından bisiklet kiraladı.");
                    }
                }
                musteriBul(ID, localRoot.rightChild);

            }
        }
        public void bisikletKirala(String istasyon, int ID, TreeNode localRoot)
        {
            Random r = new Random();
            Müşteri müşteri = new Müşteri(ID, r.Next(24), r.Next(60));

            if (localRoot != null)
            {
                bisikletKirala(istasyon, ID, localRoot.leftChild);
                if (localRoot.data.DurakAdi == istasyon)
                {
                    localRoot.data.BosPark++;
                    localRoot.data.NormalSayisi--;
                    localRoot.data.kiralayan_müşteri_sayısı++;
                    localRoot.data.müşteriler.Add(müşteri);
                    System.Console.WriteLine("Bisiklet kiralama başarılı!");
                }

                bisikletKirala(istasyon, ID, localRoot.leftChild);
            }

        }


    }

    class Program
    {
        static void Main(string[] args)
        {
            Random r = new Random();
            Tree DurakAğacı = new Tree();
            String[] duraklar = { "İnciraltı, 28, 2, 10", "Sahilevleri, 8, 1, 11", "Doğal Yaşam Parkı, 17, 1, 6", "Bostanlı İskele, 7, 0, 5", "Fethi Sekin Parkı, 6, 3, 6", "Cumhuriyet Parkı, 6, 0, 4", "Bornova Stad, 6, 1, 5", "Bornova Metro, 7, 2, 5", "Meles Rekreasyon Alanı, 15, 7, 7" };
            List<Müşteri> kiralayan_müşteriler_listesi;
            int kiralayan_müşteri_sayısı;
            Müşteri müşteri;
            int saat;
            int dakika;
            int ID;

            for (int i = 0; i < duraklar.Length; i++)
            {
                String durak = duraklar[i];
                String[] durakx = durak.Split(',');
                int NormalSayisi = Int16.Parse(durakx[3]);
                int Bospark = Int16.Parse(durakx[1]);
                kiralayan_müşteri_sayısı = r.Next(NormalSayisi);


                kiralayan_müşteriler_listesi = new List<Müşteri>(kiralayan_müşteri_sayısı);
                NormalSayisi -= kiralayan_müşteri_sayısı;
                Bospark += kiralayan_müşteri_sayısı;


                for (int j = 1; j < kiralayan_müşteri_sayısı + 1; j++)
                {
                    ID = r.Next(1, 21);
                    saat = r.Next(24);
                    dakika = r.Next(60);
                    müşteri = new Müşteri(ID, saat, dakika);
                    kiralayan_müşteriler_listesi.Add(müşteri);
                }

                Duraklar durakNesne = new Duraklar(durakx[0], Int16.Parse(durakx[1]) + kiralayan_müşteri_sayısı, Int16.Parse(durakx[2]), Int16.Parse(durakx[3]) - kiralayan_müşteri_sayısı, kiralayan_müşteriler_listesi, kiralayan_müşteri_sayısı);

                DurakAğacı.insert(durakNesne);

            }

            DurakAğacı.inOrder(DurakAğacı.getRoot());
            DurakAğacı.derinlikBul(DurakAğacı.getRoot(), duraklar.Length);
            string IDv;
            int arananID;
            System.Console.Write("\n\nMüşteri ID'si:");
            IDv = System.Console.ReadLine();
            arananID = Int16.Parse(IDv);
            DurakAğacı.musteriBul(arananID, DurakAğacı.getRoot());
            string istasyon;
            int kartID;
            System.Console.Write("\n\nBisiklet kiralama sistemine hoşgeldiniz.. Müşteri ID'nizi giriniz:");
            kartID = Convert.ToInt16(System.Console.ReadLine());
            System.Console.Write("\n\nKiralamak istediğiniz istasyonun adını girin:");
            istasyon = System.Console.ReadLine();
            DurakAğacı.bisikletKirala(istasyon, kartID, DurakAğacı.getRoot());
            System.Console.ReadLine();
            DurakAğacı.inOrder(DurakAğacı.getRoot());
            System.Console.ReadLine();
            Hashtable DurakHash = new Hashtable();
            for (int i = 0; i < duraklar.Length; i++)
            {
                String durak = duraklar[i];
                String[] durakx = durak.Split(',');
                String durakadi = durakx[0];
                int BP = Int16.Parse(durakx[1]);
                int TB = Int16.Parse(durakx[2]);
                int NB = Int16.Parse(durakx[3]);
                if (BP > 5)
                {
                    Duraklar durakNesne = new Duraklar(durakadi, BP - 5, TB, NB + 5);
                    DurakHash.Add(i, durakNesne);
                }
                else
                {
                    Duraklar durakNesne = new Duraklar(durakadi, BP, TB, NB);
                    DurakHash.Add(i, durakNesne);
                }

            }
            Heap durakHeap = new Heap(duraklar.Length);
            
            String[] enCok3Bisiklet=new string[3];
            int encok = 0;
            for (int i = 0; i < duraklar.Length; i++)
            {
                String durak = duraklar[i];
                String[] durakx = durak.Split(',');
                String durakadi = durakx[0];
                int BP = Int16.Parse(durakx[1]);
                int TB = Int16.Parse(durakx[2]);
                int NB = Int16.Parse(durakx[3]);
                durakHeap.insert(NB);
                if (encok < NB)
                {
                    encok = NB;
                    enCok3Bisiklet.Append(durakadi + " " + BP + " " + TB + " " + NB);
                }

            }
            durakHeap.displayHeap();
            System.Console.WriteLine(enCok3Bisiklet[0]);
            System.Console.WriteLine(enCok3Bisiklet[1]);
            System.Console.WriteLine(enCok3Bisiklet[2]);

            System.Console.ReadLine();
        }
    }
    class Müşteri
    {

        public int ID;
        public int saat;
        public int dakika;
        public String kiralama_saati;
        public Müşteri(int ID, int saat, int dakika)
        {

            this.ID = ID;
            this.saat = saat;
            this.dakika = dakika;
            this.kiralama_saati = saat + ":" + dakika;

        }

    }
    class Duraklar
    {
        public String DurakAdi;
        public int BosPark;
        public int TandemSayisi;
        public int NormalSayisi;
        public List<Müşteri> müşteriler;
        Random r = new Random();
        public int kiralayan_müşteri_sayısı;

        public Duraklar(String DurakAdi, int Bospark, int TandemSayisi, int NormalSayisi, List<Müşteri> müşteriler, int kiralayan_müşteri_sayısı)
        {



            this.DurakAdi = DurakAdi;
            this.BosPark = Bospark;
            this.TandemSayisi = TandemSayisi;
            this.NormalSayisi = NormalSayisi;
            this.müşteriler = müşteriler;
            this.kiralayan_müşteri_sayısı = kiralayan_müşteri_sayısı;
        }
        public Duraklar(String DurakAdi, int Bospark, int TandemSayisi, int NormalSayisi)
        {
            this.DurakAdi = DurakAdi;
            this.BosPark = Bospark;
            this.TandemSayisi = TandemSayisi;
            this.NormalSayisi = NormalSayisi;
        }
        public void müşterileri_yazdir(List<Müşteri> kiralayan_müşteriler_listesi)
        {
            for (int i = 0; i < kiralayan_müşteriler_listesi.Count; i++)
            {
                System.Console.WriteLine((i + 1) + ". müşteri ID:" + kiralayan_müşteriler_listesi.ElementAt(i).ID + "  Kiralama Saati: " + kiralayan_müşteriler_listesi.ElementAt(i).kiralama_saati);
            }
        }




    }
    class Node
    {
        public int iData;

        public Node(int key)
        {
            iData = key;
        }
        public int getKey()
        {
            return iData;
        }
        public void setKey(int id)
        {
            iData = id;
        }

    }
    class Heap
    {
        public Node[] heapArray;
        public int maxSize;
        public int currentSize;
        public Heap(int mx)
        {
            maxSize = mx;
            currentSize = 0;
            heapArray = new Node[maxSize];


        }
        public Boolean isEmpty() { return currentSize == 0; }
        public Boolean insert(int key)
        {
            if (currentSize == maxSize)
            {
                return false;
            }
            Node newNode = new Node(key);
            heapArray[currentSize] = newNode;
            trickleUp(currentSize++);
            return true;
        }
        public void trickleUp(int index)
        {
            int parent = (index - 1) / 2;
            Node bottom = heapArray[index];
            while (index > 0 && (heapArray[parent].getKey() < bottom.getKey()))
            {
                heapArray[index] = heapArray[parent];
                index = parent;
                parent = (parent - 1) / 2;

            }
            heapArray[index] = bottom;

        }
        public void displayHeap()
        {
            System.Console.WriteLine("heapArray: ");
            for (int m = 0; m < currentSize; m++)
                if (heapArray[m] != null)
                    System.Console.WriteLine(heapArray[m].getKey() + " ");
                else
                    System.Console.WriteLine("-- ");
            System.Console.WriteLine();
            int nBlanks = 32;
            int itemsPerRow = 1;
            int column = 0;
            int j = 0;
            String dots = "...............................";
            System.Console.WriteLine(dots + dots);
            while (currentSize > 0)
            {
                if (column == 0)
                {
                    for (int k = 0; k < nBlanks; k++)
                        System.Console.Write(' ');
                }
                System.Console.Write(heapArray[j].getKey());
                if (++j == currentSize) 
                    break;
                if (++column == itemsPerRow) 
                {
                    nBlanks /= 2; 
                    itemsPerRow *= 2; 
                    column = 0; 
                    System.Console.WriteLine(); 
                }
                else 
                    for (int k = 0; k < nBlanks * 2 - 2; k++)
                    {


                        System.Console.Write(' ');
                    }
                System.Console.WriteLine("\n" + dots + dots);

            }
        }

    }
}


