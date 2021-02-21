package glmine;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Random;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.Timer;

/**
 * @author lele
 *
 */
public class Mine implements ActionListener, MouseListener {
	int ROW = 20;
	int COL = 20;
	int [][] data = new int[ROW][COL];
	int [][] flag = new int[ROW][COL];
	int MINECODE = -1;//表示是雷
	int seconds = 0;
	int minesetted=0;
	JButton[][] btns = new JButton[ROW][COL];
	String nandu = JOptionPane.showInputDialog("请输入地雷数量","3");

	
	int minecount = Integer.parseInt(nandu);
	
	int unopened = ROW*COL;
	int opened = 0;
	Color myBackColor = new Color(119,221,172);
	Color flagColor = new Color(89,80,211);
	JFrame frame = new JFrame();
	ImageIcon bannerIcon = new ImageIcon("banner.png");
	ImageIcon guessIcon = new ImageIcon("guess.png");
	ImageIcon bombIcon = new ImageIcon("bomb.png");
	ImageIcon failIcon = new ImageIcon("fail.png");
	ImageIcon winFlagIcon = new ImageIcon("win_flag.png");
	ImageIcon winIcon = new ImageIcon("win.png");
	ImageIcon flagIcon = new ImageIcon("flag.png");

	JButton bannerBtn = new JButton(bannerIcon);
	JLabel label1 = new JLabel("已扫："+ opened);
	JLabel label2 = new JLabel("待扫："+ unopened);
	JLabel label3 = new JLabel("用时："+ seconds+ "s");
	Timer timer = new Timer(1000, this);
	//定义数据结构
	
	
	
	
	
	//定义函数============================================================================================================================================
	public Mine() {
		frame.setSize(999,999);
		frame.setResizable(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLayout(new BorderLayout());
		
		setHeader();
		//addMine();
		
		setButtons();
		timer.start();
		frame.setVisible(true);
	}
	
	private void addMine(int x,int y) {
		Random rand = new Random();
		for (int i = 0; i <minecount;) {
			int r = rand.nextInt(ROW);
			int c = rand.nextInt(COL);
			if(x==r&&y==c)continue;
			if(data[r][c] != MINECODE) {
				data[r][c] = MINECODE;
				i++;
				
			}
		}
		
		//计算周边雷的数量
		for (int i = 0; i < ROW; i++) {
			for (int j = 0; j < COL; j++) {
				if (data[i][j] == MINECODE) continue;
				int tempCount = 0;//雷数计数
				if (i>0 && j>0 && data[i-1][j-1]==MINECODE) tempCount++;
				if (i>0 && data[i-1][j]==MINECODE) tempCount++;
				if (i>0 && j<COL-1 && data[i-1][j+1]==MINECODE) tempCount++;
				if (j>0 && data[i][j-1]==MINECODE) tempCount++;
				if (j<COL-1 && data[i][j+1]==MINECODE) tempCount++;
				if (i<ROW-1&& j>0 && data[i+1][j-1]==MINECODE) tempCount++;
				if (i<ROW-1&& data[i+1][j]==MINECODE) tempCount++;
				if (i<ROW-1 && j<COL-1 && data[i+1][j+1]==MINECODE) tempCount++;
				data[i][j]=tempCount;
			}
		}
	}
	
	private void setButtons() {
		Container con = new Container();
		con.setLayout(new GridLayout(ROW,COL));
		
		for (int i = 0; i < ROW; i++) {
			for (int j = 0; j < COL; j++) {
				JButton btn = new JButton(guessIcon);
				//JButton btn = new JButton(data[i][j]+"");//+""转换为字符串
				btn.setOpaque(true);
				btn.setBackground(new Color(244,183,113));
				btn.addActionListener(this);
				con.add(btn);
				btns[i][j] = btn;
				btns[i][j].addMouseListener(this);
			}
		}
		
		frame.add(con, BorderLayout.CENTER);
	}
	
	private void setHeader() {
		// TODO Auto-generated method stub
		JPanel panel = new JPanel(new GridBagLayout());
		GridBagConstraints c1 = new GridBagConstraints(0,0,3,1,1.0,1.0,GridBagConstraints.CENTER ,GridBagConstraints.BOTH, new Insets(0, 0, 0, 0), 0, 0);
		panel.add(bannerBtn,c1);
		bannerBtn.addActionListener(this);
		
		label1.setOpaque(true);
		label1.setBackground(Color.white);
		label1.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY ));
		
		label2.setOpaque(true);
		label2.setBackground(Color.white);
		label2.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY ));
		
		label3.setOpaque(true);
		label3.setBackground(Color.white);
		label3.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY ));
		
		GridBagConstraints c2 = new GridBagConstraints(0,1,1,1,1.0,1.0,GridBagConstraints.CENTER ,GridBagConstraints.BOTH, new Insets(0, 0, 0, 0), 0, 0);
		panel.add(label1,c2);
		GridBagConstraints c3 = new GridBagConstraints(1,1,1,1,1.0,1.0,GridBagConstraints.CENTER ,GridBagConstraints.BOTH, new Insets(0, 0, 0, 0), 0, 0);
		panel.add(label2,c3);
		GridBagConstraints c4 = new GridBagConstraints(2,1,1,1,1.0,1.0,GridBagConstraints.CENTER ,GridBagConstraints.BOTH, new Insets(0, 0, 0, 0), 0, 0);
		panel.add(label3,c4);
		
		
		
		
		frame.add(panel, BorderLayout.NORTH);
	}

	public void mouseClicked(MouseEvent e) {
		JButton btn = (JButton)e.getSource();
		for (int i = 0; i < ROW; i++) {
			for (int j = 0; j < COL; j++) {
				if(btn.equals(btns[i][j])) {
					if(e.getButton()==MouseEvent.BUTTON3) {
						if(btn.isEnabled()) {
							if(flag[i][j]==0) {
								flag[i][j]=1;
								btn.setIcon(flagIcon);
								btn.setOpaque(true);
								btn.setBackground(flagColor);
								btn.setText("");
								
							}else {
								flag[i][j]=0;
								btn.setIcon(guessIcon);
								btn.setOpaque(true);
								btn.setBackground(new Color(244,183,113));
								btn.setText("");
							}
						}
					}
				}
			}
		}
	}
	
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() instanceof Timer) {
			seconds++;
			label3.setText("用时："+ seconds+ "s");
			timer.start();
			return;
		}
		JButton btn = (JButton)e.getSource();
		if(btn.equals(bannerBtn)) {
			restart();
			return;
		}
		for (int i = 0; i < ROW; i++) {
			for (int j = 0; j < COL; j++) {
				if(btn.equals(btns[i][j])) {
					if(minesetted==0) {
						addMine(i, j);
						minesetted=1;
					}else {
						
					
						if(data[i][j]==MINECODE) {
							lose();
						}else {
							openCell(i, j);
							checkWin();
						}
						
						
						return;
					}
				}
			}
		}
	}
	
	private void checkWin() {
		int count =0;
		for (int i = 0; i < ROW; i++) {
			for (int j = 0; j < COL; j++) {
				if(btns[i][j].isEnabled()) count++;
			}
		}
		if (count == minecount) {
			for (int i = 0; i < ROW; i++) {
				for (int j = 0; j < COL; j++) {
					if(btns[i][j].isEnabled()) {
						btns[i][j].setIcon(winFlagIcon);
					}
				}
			}
			bannerBtn.setIcon(winIcon);
			timer.stop();
			JOptionPane.showMessageDialog(frame, "你赢了！！！Yeah！！\n点击上方按钮重新开始","恭喜你",JOptionPane.PLAIN_MESSAGE);
			
		}
		
	}
	
	
	
	private void lose() {
		bannerBtn.setIcon(failIcon);
		timer.stop();
		for (int i = 0; i < ROW; i++) {
			for (int j = 0; j < COL; j++) {
				if(btns[i][j].isEnabled()) {
					JButton btn = btns[i][j];
					if(data[i][j] == MINECODE) {
						btn.setEnabled(false);
						btn.setIcon(bombIcon);
						btn.setDisabledIcon(bombIcon);
						
					}else {
						btn.setIcon(null);
						btn.setEnabled(false);
						btn.setOpaque(true);
						//btn.setBackground(myBaclColor);
						btn.setText(data[i][j]+"");
					}
				}
			}
		}
		JOptionPane.showMessageDialog(frame, "踩到雷了！！！\n点击上方按钮重新开始","喔嚯",JOptionPane.PLAIN_MESSAGE);

	}

	private void openCell(int i,int j) {
		JButton btn = btns[i][j];
		btn.setMargin(new Insets(0, 0, 0, 0));
		if (!btn.isEnabled()) return;
		
		btn.setIcon(null);
		btn.setEnabled(false);
		btn.setOpaque(true);
		btn.setBackground(myBackColor);
		btn.setText(data[i][j]+"");
		addOpencount();
		
		
		if(data[i][j] >0) {
			openCell(i, j);
		}
		

		
		if(data[i][j] == 0) {
			if (i>0 && j>0) openCell(i-1, j-1);
			if (i>0) openCell(i-1, j);
			if (i>0 && j<COL-1) openCell(i-1, j+1);
			if (j>0 ) openCell(i, j-1);
			if (j<COL-1) openCell(i, j+1);
			if (i<ROW-1&& j>0) openCell(i+1, j-1);
			if (i<ROW-1) openCell(i+1, j);
			if (i<ROW-1 && j<COL-1) openCell(i+1, j+1);
		
		
		}
//		if(data[i][j] != MINECODE) {
//			if (i>0 && j>0 && data[i-1][j-1]==0) openCell(i-1, j-1);
//			if (i>0 && data[i-1][j]==0) openCell(i-1, j);
//			if (i>0 && j<COL-1 && data[i-1][j+1]==0) openCell(i-1, j+1);
//			if (j>0 && data[i][j-1]==0) openCell(i, j-1);
//			if (j<COL-1 && data[i][j+1]==0) openCell(i, j+1);
//			if (i<ROW-1&& j>0 && data[i+1][j-1]==0) openCell(i+1, j-1);
//			if (i<ROW-1&& data[i+1][j]==0) openCell(i+1, j);
//			if (i<ROW-1 && j<COL-1 && data[i+1][j+1]==0) openCell(i+1, j+1);
//		
//		
//		}
//		if(data[i][j] == 0) {
//			if (i>0 && j>0) openCell(i-1, j-1);
//			if (i>0 ) openCell(i-1, j);
//			if (i>0 && j<COL-1) openCell(i-1, j+1);
//			if (j>0) openCell(i, j-1);
//			if (j<COL-1) openCell(i, j+1);
//			if (i<ROW-1&& j>0) openCell(i+1, j-1);
//			if (i<ROW-1) openCell(i+1, j);
//			if (i<ROW-1) openCell(i+1, j+1);
//		
//		
//		}
		
	}
	
	private void addOpencount() {
		opened++;
		unopened--;
		label1.setText("已扫："+ opened);
		label2.setText("待扫："+ unopened);
	}
	
	private void restart() {
		/*
		 * 1.数据清零
		 * 2.按钮恢复
		 * 3.重新启动时钟
		 */
		minesetted=0;
		for (int i = 0; i < ROW; i++) {
			for (int j = 0; j < COL; j++) {
				data[i][j]=0;
				btns[i][j].setBackground(new Color(244,183,133));
				btns[i][j].setEnabled(true);
				btns[i][j].setText("");
				btns[i][j].setIcon(guessIcon);
			}
		}
		//minecount = 3;
		unopened = ROW*COL;
		opened = 0;
		seconds = 0;
		bannerBtn.setIcon(bannerIcon);
		timer.start();
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			new Mine();
			
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	
}
