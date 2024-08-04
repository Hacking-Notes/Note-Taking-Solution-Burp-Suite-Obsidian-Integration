import os
from threading import Thread
from burp import IBurpExtender, ITab
from javax.swing import JPanel, JButton, JTextField, JFileChooser, JLabel, JOptionPane, JCheckBox, BorderFactory
from java.awt import GridBagLayout, GridBagConstraints, Insets, Color, Dimension, Font
from java.net import URL

class BurpExtender(IBurpExtender, ITab):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        # Set the extension name
        callbacks.setExtensionName("Obsidian")
        
        # Create and add the custom tab
        self._tab = JPanel(GridBagLayout())
        self._tab.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10))
        
        constraints = GridBagConstraints()
        constraints.fill = GridBagConstraints.HORIZONTAL
        constraints.insets = Insets(5, 5, 5, 5)
        
        # Add description label
        constraints.gridx = 0
        constraints.gridy = 0
        constraints.gridwidth = 3
        self._descriptionLabel = JLabel("Request to Import to Obsidian")
        self._descriptionLabel.setForeground(Color.WHITE)
        self._descriptionLabel.setFont(Font("Arial", Font.BOLD, 16))
        self._tab.add(self._descriptionLabel, constraints)
        
        # Add vertical space (empty label)
        constraints.gridx = 0
        constraints.gridy = 1
        constraints.gridwidth = 2
        self._verticalSpace = JLabel(" ")
        self._tab.add(self._verticalSpace, constraints)

        # Save folder location label
        constraints.gridx = 0
        constraints.gridy = 2
        constraints.gridwidth = 1
        self._label = JLabel("Save folder location:")
        self._tab.add(self._label, constraints)
        
        # Folder path field
        constraints.gridx = 1
        constraints.gridy = 2
        self._folderPathField = JTextField(20)
        self._tab.add(self._folderPathField, constraints)
        
        # Browse button
        constraints.gridx = 2
        constraints.gridy = 2
        self._browseButton = JButton("Browse")
        self._browseButton.addActionListener(self._browse)
        self._tab.add(self._browseButton, constraints)
        
        # Create checkboxes for HTTP, HTTPS, and both
        constraints.gridx = 0
        constraints.gridy = 3
        self._httpCheckBox = JCheckBox("HTTP")
        self._httpCheckBox.addActionListener(self._updateCheckboxes)
        self._tab.add(self._httpCheckBox, constraints)
        
        constraints.gridx = 1
        constraints.gridy = 3
        self._httpsCheckBox = JCheckBox("HTTPS", True)  # Default to checked
        self._httpsCheckBox.addActionListener(self._updateCheckboxes)
        self._tab.add(self._httpsCheckBox, constraints)
        
        constraints.gridx = 2
        constraints.gridy = 3
        self._httpAndHttpsCheckBox = JCheckBox("HTTP & HTTPS")
        self._httpAndHttpsCheckBox.addActionListener(self._updateCheckboxes)
        self._tab.add(self._httpAndHttpsCheckBox, constraints)
        
        # Add vertical space (empty label)
        constraints.gridx = 0
        constraints.gridy = 1
        constraints.gridwidth = 2
        self._verticalSpace = JLabel(" ")
        self._tab.add(self._verticalSpace, constraints)
        
        # Generate button positioned below the checkboxes
        constraints.gridx = 0
        constraints.gridy = 4
        constraints.gridwidth = 1
        self._generateButton = JButton("Generate")
        self._generateButton.setPreferredSize(Dimension(100, 30))
        self._descriptionLabel.setForeground(Color(255, 255, 255))
        self._generateButton.setBackground(Color(238, 103, 0))  # Orange color
        self._generateButton.setOpaque(True)
        self._generateButton.setBorderPainted(False)
        self._generateButton.addActionListener(self._generate)
        self._tab.add(self._generateButton, constraints)
        
        # Loading label
        constraints.gridx = 1
        constraints.gridy = 4
        constraints.gridwidth = 2
        self._loadingLabel = JLabel("")
        self._tab.add(self._loadingLabel, constraints)
        
        # Message label
        constraints.gridx = 0
        constraints.gridy = 5
        constraints.gridwidth = 3
        self._messageLabel = JLabel("")
        self._messageLabel.setForeground(Color(0, 128, 0))
        self._tab.add(self._messageLabel, constraints)
        
        # Add the custom tab to Burp Suite
        callbacks.addSuiteTab(self)

    
    def getTabCaption(self):
        return "Obsidian"
    
    def getUiComponent(self):
        return self._tab
    
    def _browse(self, event):
        # Create a JFileChooser configured for directory selection
        file_chooser = JFileChooser()
        file_chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
        result = file_chooser.showSaveDialog(None)
        if result == JFileChooser.APPROVE_OPTION:
            folder = file_chooser.getSelectedFile()
            self._folderPathField.setText(folder.getAbsolutePath())
    
    def _updateCheckboxes(self, event):
        source = event.getSource()
        if source == self._httpCheckBox:
            if self._httpCheckBox.isSelected():
                self._httpsCheckBox.setSelected(False)
                self._httpAndHttpsCheckBox.setSelected(False)
        elif source == self._httpsCheckBox:
            if self._httpsCheckBox.isSelected():
                self._httpCheckBox.setSelected(False)
                self._httpAndHttpsCheckBox.setSelected(False)
        elif source == self._httpAndHttpsCheckBox:
            if self._httpAndHttpsCheckBox.isSelected():
                self._httpCheckBox.setSelected(False)
                self._httpsCheckBox.setSelected(False)
    
    def _generate(self, event):
        # Show loading message
        self._loadingLabel.setText("Loading...")
        
        # Run the generation process in a new thread
        thread = Thread(target=self._generate_in_thread)
        thread.start()
    
    def _generate_in_thread(self):
        folder_path = self._folderPathField.getText()
        if not folder_path:
            JOptionPane.showMessageDialog(None, "Please specify a folder path.", "Error", JOptionPane.ERROR_MESSAGE)
            self._loadingLabel.setText("")
            return
        
        # Determine selected protocols
        selected_protocols = set()
        if self._httpCheckBox.isSelected():
            selected_protocols.add("http")
        if self._httpsCheckBox.isSelected():
            selected_protocols.add("https")
        if self._httpAndHttpsCheckBox.isSelected():
            selected_protocols.add("http")
            selected_protocols.add("https")

        # Ensure at least one protocol is selected
        if not selected_protocols:
            JOptionPane.showMessageDialog(None, "Please select at least one protocol.", "Error", JOptionPane.ERROR_MESSAGE)
            self._loadingLabel.setText("")
            return
        
        # Fetch URLs based on the selected protocols
        if "http" in selected_protocols and "https" in selected_protocols:
            urls = self._get_unique_urls_in_scope()
        else:
            urls = self._get_filtered_urls_in_scope("http" in selected_protocols, "https" in selected_protocols)
        
        if not urls:
            self._messageLabel.setText("No URLs in scope.")
            self._loadingLabel.setText("")
            return
        
        # Process URLs to create folder structure and include request details
        try:
            self._create_folder_structure(folder_path, urls)
            self._messageLabel.setText("Folder structure created in {}".format(folder_path))
        except Exception as e:
            JOptionPane.showMessageDialog(None, "An error occurred: {}".format(str(e)), "Error", JOptionPane.ERROR_MESSAGE)
            self._messageLabel.setText("Failed to create folder structure.")
        
        self._loadingLabel.setText("")
    
    def _get_filtered_urls_in_scope(self, http_selected, https_selected):
        urls = set()
        http_protocol = "http"
        https_protocol = "https"
        
        # Get the list of IHttpRequestResponse objects in the target scope
        http_messages = self._callbacks.getProxyHistory()
        for message in http_messages:
            url = self._helpers.analyzeRequest(message).getUrl()
            url_str = url.toString()
            
            if self._callbacks.isInScope(url):
                if (http_selected and url.getProtocol() == http_protocol and not https_selected) or \
                   (https_selected and url.getProtocol() == https_protocol):
                    urls.add(url_str)
        
        return urls
    
    def _get_unique_urls_in_scope(self):
        urls = set()
        # Get the list of IHttpRequestResponse objects in the target scope
        http_messages = self._callbacks.getProxyHistory()
        for message in http_messages:
            url = self._helpers.analyzeRequest(message).getUrl()
            if self._callbacks.isInScope(url):
                urls.add(url.toString())
        return urls
    
    def _create_folder_structure(self, base_folder, urls):
        for url_str in urls:
            try:
                url = URL(url_str)
                # Get the path and clean it
                path = url.getPath().strip("/")
                # Replace ':' with empty string in the path
                path = path.replace(":", "")
                
                # Construct folder paths
                tld_folder = url.getHost().split('.')[-2] + '.' + url.getHost().split('.')[-1]
                subfolders = [url.getHost()] + path.split('/')
                
                current_path = os.path.join(base_folder, tld_folder)
                folder_exists = os.path.exists(current_path)

                for subfolder in subfolders:
                    current_path = os.path.join(current_path, subfolder)
                    if not os.path.exists(current_path):
                        os.makedirs(current_path)
                        folder_exists = False
                
                # Always create root.md in the subdomain folder
                subdomain_path = os.path.join(base_folder, tld_folder, url.getHost())
                root_md_path = os.path.join(subdomain_path, "root.md")
                if not os.path.exists(root_md_path):
                    with open(root_md_path, 'w') as md_file:
                        md_file.write(self._get_request(url_str))

                # Only create .md file if the folder did not exist
                if not folder_exists:
                    if not path:
                        md_file_path = os.path.join(current_path, "root.md")
                    else:
                        last_segment = subfolders[-1]
                        md_file_path = os.path.join(current_path, "{}.md".format(last_segment))
                    
                    if not os.path.exists(md_file_path):
                        with open(md_file_path, 'w') as md_file:
                            md_file.write(self._get_request(url_str))
            except Exception as e:
                raise RuntimeError("Failed to create folder structure for URL '{}': {}".format(url_str, str(e)))

    def _get_request(self, url_str):
        # Get the list of IHttpRequestResponse objects in the target scope
        http_messages = self._callbacks.getProxyHistory()
        for message in http_messages:
            url = self._helpers.analyzeRequest(message).getUrl()
            if url.toString() == url_str:
                request_info = self._helpers.analyzeRequest(message)
                headers = request_info.getHeaders()
                body = message.getRequest()[request_info.getBodyOffset():]
                
                # Format request data
                request_data = "## Request" + "\n\n" + "```\n" + "\n".join(headers) + "\n\n" + self._helpers.bytesToString(body) + "\n" + "```" + "\n\n" + "## Information"
                return request_data
        return "Request data not found for URL: {}".format(url_str)
