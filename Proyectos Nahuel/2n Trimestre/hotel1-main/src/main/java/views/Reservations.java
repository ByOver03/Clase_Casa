package views;

public class Reservations extends javax.swing.JPanel {

    public Reservations() {
        initComponents();
        InitStyles();
    }
    
    private void InitStyles() {
        
    }
   
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        bg = new javax.swing.JPanel();
        roomNText = new javax.swing.JLabel();
        roomNField = new javax.swing.JTextField();
        startDateText = new javax.swing.JLabel();
        startDateField = new javax.swing.JFormattedTextField();
        endDateText = new javax.swing.JLabel();
        endDateField = new javax.swing.JFormattedTextField();
        reserve = new javax.swing.JButton();

        setBackground(new java.awt.Color(255, 255, 255));

        bg.setBackground(new java.awt.Color(255, 255, 255));

        roomNText.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        roomNText.setText("Enter the room number");

        roomNField.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                roomNFieldActionPerformed(evt);
            }
        });

        startDateText.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        startDateText.setText("Enter the start date");

        startDateField.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                startDateFieldActionPerformed(evt);
            }
        });

        endDateText.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        endDateText.setText("Enter the end date");

        reserve.setBackground(new java.awt.Color(13, 71, 161));
        reserve.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        reserve.setForeground(new java.awt.Color(255, 255, 255));
        reserve.setText("Reserve");
        reserve.setBorderPainted(false);
        reserve.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        reserve.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                reserveActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout bgLayout = new javax.swing.GroupLayout(bg);
        bg.setLayout(bgLayout);
        bgLayout.setHorizontalGroup(
            bgLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(bgLayout.createSequentialGroup()
                .addGroup(bgLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(bgLayout.createSequentialGroup()
                        .addGap(25, 25, 25)
                        .addGroup(bgLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(bgLayout.createSequentialGroup()
                                .addComponent(endDateText, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGap(41, 41, 41))
                            .addGroup(bgLayout.createSequentialGroup()
                                .addComponent(startDateText, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGap(36, 36, 36))
                            .addComponent(roomNText, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(roomNField)
                            .addComponent(startDateField)
                            .addComponent(endDateField, javax.swing.GroupLayout.Alignment.TRAILING)))
                    .addGroup(bgLayout.createSequentialGroup()
                        .addGap(31, 31, 31)
                        .addComponent(reserve, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addGap(8, 8, 8)))
                .addGap(539, 539, 539))
        );
        bgLayout.setVerticalGroup(
            bgLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(bgLayout.createSequentialGroup()
                .addGap(62, 62, 62)
                .addComponent(roomNText, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(roomNField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(startDateText, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(startDateField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(endDateText, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(endDateField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(reserve)
                .addGap(128, 128, 128))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(this);
        this.setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(bg, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGap(0, 0, 0))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addComponent(bg, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGap(0, 0, 0))
        );
    }// </editor-fold>//GEN-END:initComponents

    private void roomNFieldActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_roomNFieldActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_roomNFieldActionPerformed

    private void startDateFieldActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_startDateFieldActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_startDateFieldActionPerformed

    private void reserveActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_reserveActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_reserveActionPerformed


    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel bg;
    private javax.swing.JFormattedTextField endDateField;
    private javax.swing.JLabel endDateText;
    private javax.swing.JButton reserve;
    private javax.swing.JTextField roomNField;
    private javax.swing.JLabel roomNText;
    private javax.swing.JFormattedTextField startDateField;
    private javax.swing.JLabel startDateText;
    // End of variables declaration//GEN-END:variables
}