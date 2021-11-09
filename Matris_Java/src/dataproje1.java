

public class dataproje1 {

	public static void main(String[] args) {
		
		distanceMatris(rastgeleSayiUret(100,100,10),10);
        
		
	}
	
	static double[][] rastgeleSayiUret(int width,int height,int n) {

        double matris[][] = new double[n][2];
        
        for(int i =0;i<n;i++){
            matris[i][0]=(double)Math.random()*width;
            matris[i][1]=(double)Math.random()*height;
        }
        
        for(int j=0;j<n;j++){
            System.out.println((j+1)+". point:  "+matris[j][0]+"   "+matris[j][1]);
        }
        return matris;
	}
	static double[][] distanceMatris(double[][] matris,int n){
		double DM[][] = new double[n][n];
		
		for (int i = 0; i<n;i++) {
			for(int j = 0;j<n;j++) {
				double x1,x2,y1,y2;
				x1 = matris[j][0];
				y1 = matris[j][1];
				x2 = matris[i][0];
				y2 = matris[i][1];
				DM[i][j] = Math.sqrt(Math.abs((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)));
			}
			
		}
		for (int i = 0; i<n;i++) {
			for(int j = 0;j<n;j++) {
				System.out.print(DM[i][j]+" ");
			}
			System.out.print("\n");
		}
		
		return DM;
	}

}
