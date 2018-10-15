    <?php 
        public function callback()
        {
        try {
            // Set the response content type to application/json
            header("Content-Type:application/json");
            $resp = '{"ResultCode":0,"ResultDesc":"Result message well received"}';
            // read incoming request message body
            $postData = file_get_contents('php://input');
            // open text file for logging messages by appending
            $filePath = "messages.log";
            // error log
            $errorLog = "\errors.log";
            // Parse payload to json
            $file = fopen($filePath, "a");
            // log response and close file
            fwrite($file, $postData);
            fwrite($file, "\r\n");
            fclose($file);
            // Parse message body to json payload
            $jdata = json_decode($postData, true);
            
            $flatArray = new RecursiveIteratorIterator(new RecursiveArrayIterator($jdata));
            $list = iterator_to_array($flatArray, false);
        } catch (Exception $ex) {
            // append exception to file
            $logErr = fopen($errorLog, "a");
            fwrite($logErr, $ex->getMessage());
            fwrite($logErr, "\r\n");
            ;
            // $resp = '{"ResultCode": 1, "ResultDesc":"Validation failure due to internal service error"}';
        }
        // log response and close the file
        fwrite($file, $resp);
        fclose($file);
        // echo response
        echo $resp;
    }

    public function confirmation()
    {
        $this->load->model('mpesaapi_model');
        // Create a C2B confirmation call back URL to your website
        try {
            // Set the response content type to application/json
            header("Content-Type:application/json");
            $resp = '{"ResultCode":0,"ResultDesc":"Result message well received"}';
            // read incoming request message body
            $postData = file_get_contents('php://input');
            // open text file for logging messages by appending
            $filePath = "messages.log";
            // error log
            $errorLog = "\errors.log";
            // Parse payload to json
            $file = fopen($filePath, "a");
            // log response and close file
            fwrite($file, $postData);
            fwrite($file, "\r\n");
            fclose($file);
            // Parse message body to json payload
            $jdata = json_decode($postData, true);
            
            $flatArray = new RecursiveIteratorIterator(new RecursiveArrayIterator($jdata));
            $list = iterator_to_array($flatArray, false);
            
            $MerchantRequestID = $jdata["MerchantRequestID"];
            $CheckoutRequestID = $jdata["CheckoutRequestID"];
            $ResultCode = $jdata["ResultCode"];
            $ResultDesc = $jdata["ResultDesc"];
            $Amount = $jdata["Amount"];
            $MpesaReceiptNumber = $jdata["MpesaReceiptNumber"];
            $Balance = $jdata["Balance"];
            $TransactionDate = $jdata["TransactionDate"];
            $PhoneNumber = $jdata["PhoneNumber"];
            
            $host = "localhost"; // Host name
            $username = "root"; // Mysql username bigsofts_userm
            $password = "malio1234"; // Mysql password
            $db_name = "stoneweb_developer"; // Database name
                                             
            try {
                $conn = new PDO($servername, $username, $password, $dbname);
                // set the PDO error mode to exception
                $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                $sql = "INSERT INTO mpesaapi(MerchantRequestID, CheckoutRequestID, ResultCode, ResultDesc, Amount,MpesaReceiptNumber,Balance,TransactionDate,PhoneNumber)
          VALUES ('$MerchantRequestID','$CheckoutRequestID','$ResultCode','$ResultDesc','$Amount','$MpesaReceiptNumber','$Balance','$TransactionDate','$PhoneNumber')";
                // use exec() because no results are returned
                $conn->exec($sql);
                echo "New record created successfully";
            }
            catch(PDOException $e)
            {
                echo $sql . "<br>" . $e->getMessage();
            }
            
            $conn = null;
        } catch (Exception $ex) {
            // append exception to file
            $logErr = fopen($errorLog, "a");
            fwrite($logErr, $ex->getMessage());
            fwrite($logErr, "\r\n");
        }
        // log response and close the file
        fwrite($file, $resp);
        fclose($file);
        // echo response
        echo $resp;
    }
//     register our validation and confirmation URL’s
    public function pay()
    {
       
        header("Content-Type:application/json");
        $phone = $_POST['phonenumber'];
        // if(empty($phone)){echo "Please Enter the phone number in this format: 254722000000";}
        
        $shortcode = '174379';
        $passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919';
        $consumerkey = "mxHfXZgmIrq6aGkm0D4UOUV3ECp4g1OI";
        $consumersecret = "4KmjMiOe0sIIcnZS";
        $validationurl = "https://f01c8fee.ngrok.io/index.php/appointments/callback";
        $confirmationurl = "https://f01c8fee.ngrok.io/index.php/appointments/confirmation";
        
        /* testing environment, comment the below two lines if on production */
        $authenticationurl = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials';
        $registerurl = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl';
    
        /* production un-comment the below two lines if you are in production */
        // $authenticationurl=’https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials’;
        // $registerurl = ‘https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl’;
        $credentials = base64_encode($consumerkey . ':' . $consumersecret);
        
        // Request headers
        $headers = array(
            'Content-Type: application/json; charset=utf-8'
        );
        // Request
        $ch = curl_init($authenticationurl);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
        // curl_setopt($ch, CURLOPT_HEADER, TRUE); // Includes the header in the output
        curl_setopt($ch, CURLOPT_HEADER, FALSE); // excludes the header in the output
        curl_setopt($ch, CURLOPT_USERPWD, $consumerkey . ":" . $consumersecret); // HTTP Basic Authentication
        $result = curl_exec($ch);
        // echo $result;
        $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $result = json_decode($result);
        
        $access_token = $result->access_token;
        // var_dump($access_token);
        curl_close($ch);
        //Register urls
        $curl = curl_init();
        curl_setopt($curl, CURLOPT_URL, $registerurl);
        curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type:application/json','Authorization:Bearer '.$access_token));
        //get the timestamp
        $date = time();
        $timestamp = date("Ymdhms", $date);
        
        $password = base64_encode($shortcode . $passkey . $timestamp);
        // echo $password;
        $transactiondesc = "Successful";
        $url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest';
        $curlInitResult = curl_init($url);
        curl_setopt($curlInitResult, CURLOPT_URL, $url);
        curl_setopt($curlInitResult, CURLOPT_HTTPHEADER, array(
            'Content-Type:application/json',
            'Authorization:Bearer ' . $access_token
        ));
        
        $curl_post_data = array(
            // Fill in the request parameters with valid values
            'BusinessShortCode' => $shortcode,
            'Password' => $password,
            'Timestamp' => $timestamp,
            'TransactionType' => 'CustomerPayBillOnline',
            'Amount' => '5',
            'PartyA' => $phone,
            'PartyB' => $shortcode,
            'PhoneNumber' => $phone,
            'CallBackURL' => 'https://f01c8fee.ngrok.io/index.php/appointments/callback',
            'AccountReference' => 'AfyaResearchAfrica',
            'TransactionDesc' => $transactiondesc
        );
        // $CallbackURL = 'https://webhook.site/adca9f7a-5471-4464-b493-4d05251ec658';
        $data_string = json_encode($curl_post_data);
        curl_setopt($curlInitResult, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curlInitResult, CURLOPT_POST, true);
        curl_setopt($curlInitResult, CURLOPT_POSTFIELDS, $data_string);
        
        $curl_response = curl_exec($curlInitResult);
        print_r($curl_response);
//         $file = 'http://easyappointments.localhost/messages.log';
//         fopen($file, "r");
//         $safResp = file_get_contents($file);
//         $decoded = json_decode($safResp, true);
        
        $flatArray = new RecursiveIteratorIterator(new RecursiveArrayIterator($decoded));
        $list = iterator_to_array($flatArray, false);
        var_dump($list);
        //
    }
?>