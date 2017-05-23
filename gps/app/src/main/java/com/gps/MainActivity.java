package com.gps;

import android.app.*;
import android.os.*;
import android.widget.*;
import android.view.View.*;
import android.view.*;
import android.renderscript.*;
import java.lang.Math;
import android.icu.text.*;
import android.text.*;

public class MainActivity extends Activity 
{
    private Button calculate;
	public EditText lngs;
	public EditText lats;
	public EditText lnggp;
	public EditText latgp;
	public TextView result;
	private TextView mytextviews;
	private TextView mytextviewgp;
	@Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
		mytextviews=(TextView)findViewById(R.id.mainTextView1);
		mytextviewgp=(TextView)findViewById(R.id.mainTextView2);
		mytextviews.setText(R.string.spoint);
		mytextviewgp.setText(R.string.gppoint);
        calculate=(Button)findViewById(R.id.mainButton1);
		calculate.setText(R.string.calculate);
		lngs = (EditText)findViewById(R.id.mainEditText1);
		lats = (EditText)findViewById(R.id.mainEditText2);
		lnggp = (EditText)findViewById(R.id.mainEditText3);
		latgp = (EditText)findViewById(R.id.mainEditText4);
		result = (TextView)findViewById(R.id.mainTextView3);
		calculate.setOnClickListener(new CalculateListener());
	}
	class CalculateListener implements OnClickListener
	{

		@Override
		public void onClick(View p1)
		{
			// TODO: Implement this method
			
			String lngsstr = lngs.getText().toString();
			if(TextUtils.isEmpty(lngsstr)){
				lngs.setText("0");
				lngsstr=lngs.getText().toString();
			}
			String latsstr = lats.getText().toString();
			if(TextUtils.isEmpty(latsstr)){
				lats.setText("0");
				latsstr=lats.getText().toString();
			}
			String lnggpstr = lnggp.getText().toString();
			if(TextUtils.isEmpty(lnggpstr)){
				lnggp.setText("0");
				lnggpstr=lnggp.getText().toString();
			}
			String latgpstr = latgp.getText().toString();
			if(TextUtils.isEmpty(latgpstr)){
				latgp.setText("0");
				latgpstr=latgp.getText().toString();
			}
		    Double lngsnum = Double.parseDouble(lngsstr);
			Double latsnum = Double.parseDouble(latsstr);
			Double lnggpnum = Double.parseDouble(lnggpstr);
			Double latgpnum = Double.parseDouble(latgpstr);
			Double a = lngsnum/180.0*Math.PI;
			Double b = (latsnum)/180.0*Math.PI;
			Double c = lnggpnum/180.0*Math.PI;
			Double d = (latgpnum)/180.0*Math.PI;
			Double R = 6371004.0;
			//Double pi =3.1415926536;
			Double ac = c-a;
			Double bd = d-b;
			Double cosbd=Math.abs(Math.cos(d)/Math.cos(b));
		    Double angle=0.0;
			if(ac==0.0||bd==0.0){
				angle=null;
			}
			if(ac==0||bd>0){
				angle=0.0;
			}
			if(ac==0||bd<0){
				angle=180.0;
			}
			if(ac>0||bd==0){
				angle=90.0;
			}
			if(ac<0.0||bd==0.000000000000){
				angle=270.0;
			}
			if(ac>0||bd>0){
				angle=Math.atan(cosbd*ac/bd)*180.0/Math.PI;
			}
			else if(ac>0||bd<0){
				angle=180+Math.atan(cosbd*ac/bd)*180.0/Math.PI;
			}
			else if(ac<0||bd>0){
				angle=360+Math.atan(cosbd*ac/bd)*180.0/Math.PI;
			}
			else if(ac<0||bd<0){
				angle=180+Math.atan(cosbd*ac/bd)*180.0/Math.PI;
			}
			//Double e = Math.cos(45.0/180.0*pi);
			//Double e = Math.acos(Math.sin(b)*Math.sin(d)*Math.cos(a-c)+Math.cos(b)*Math.cos(d))*R;
			Double e = Math.acos(Math.sin(b)*Math.sin(d)+Math.cos(b)*Math.cos(d)*Math.cos(a-c))*R;
			//String res = Double.toString(e);//.format("%.2f");
			String anglestr=Double.toString(angle);
			//res1 = String.format("%.2f",2.2344);
			//res1=res;
			DecimalFormat df=new DecimalFormat("#####0.0");
			DecimalFormat df1=new DecimalFormat("#####0.00");
			String res1=df.format(e);
			anglestr=df1.format(angle);
			result.setText("距离:"+res1+"m"+"\n"+"S_GP与正北夹角"+anglestr+"º");
			if((ac==0)&&(bd==0)){
				result.setText("距离:"+res1+"m"+"\n"+"两点在同一位置");
			}
		    if(lngsnum<-180.0||lngsnum>180.0||lnggpnum<-180.0||lnggpnum>180.0||latsnum<-90.0||latsnum>90.0||latgpnum<-90.0||latgpnum>90.0){
				result.setText("坐标数据超出范围");
			}
			//result.setText(String.valueOf(e));
			//result.setText(String.valueOf(Math.acos(-1.0)));
			
		}


	}
}
