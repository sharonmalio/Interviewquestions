           <!-- PAYMENT CONFIRMATION -->
                <div id="wizard-frame-4" class="wizard-frame" style="display:none;">
                <h3 class="frame-title"><?= lang('step_six_title') ?></h3>
                            <div class="col-xs-12 col-sm-6">
                
                                    <div class="form-group">
                                        <label for="phone-number" class="control-label"><?= lang('transaction_id') ?> *</label>
                                        <input type="text" id="phone-number" class=" form-control" maxlength="60" />
                                    </div>
                            </div>
                            <?php
                                echo ' 
                                    <a href="' . site_url('appointments/pay/' . $appointment_data['hash']) . '" class="btn btn-primary btn-large">
                                        <span class="glyphicon glyphicon-usd"></span> ' .
                                        lang('pay_deposit') .'
                                    </a> ';
                                echo ' 
                                    <a href="' . site_url('appointments/pay/' . $appointment_data['hash']) . '" class="btn btn-primary btn-large">
                                        <span class="glyphicon glyphicon-usd"></span> ' .
                                        lang('pay_full_amount') .'
                                    </a> ';
                            ?> <br>
                    <div class="command-buttons">
                        <button type="button" id="button-back-3" class="btn button-back btn-primary"
                                data-step_index="3"><span class="glyphicon glyphicon-backward"></span>
                            <?= lang('back') ?>
                        </button>
                        <button type="button" id="button-next-3" class="btn button-next btn-primary"
                                data-step_index="6">
                            <?= lang('next') ?>
                            <span class="glyphicon glyphicon-forward"></span>
                        </button>
                    </div>
                </div>

                 <!-- PAYMENT CONFIRMATION -->
                 <div id="wizard-frame-4" class="wizard-frame" style="display:none;">
                <h3 class="frame-title"><?= lang('step_4_title') ?></h3>
                            <div class="col-xs-12 col-sm-6">
                
                                    <div class="form-group">
                                        <label for="phone-number" class="control-label"><?= lang('phone_number') ?> *</label>
                                        <input type="text" id="phone-number" class=" form-control" maxlength="60" />
                                    </div>
                            </div>
                            <?php
                                echo ' 
                                    <a href="' . site_url('appointments/pay/' . $appointment_data['hash']) . '" class="btn btn-primary btn-large">
                                        <span class="glyphicon glyphicon-usd"></span> ' .
                                        lang('pay_deposit') .'
                                    </a> ';
                                echo ' 
                                    <a href="' . site_url('appointments/pay/' . $appointment_data['hash']) . '" class="btn btn-primary btn-large">
                                        <span class="glyphicon glyphicon-usd"></span> ' .
                                        lang('pay_full_amount') .'
                                    </a> ';
                            ?> <br>
                         <div class="command-buttons">
                        <button type="button" id="button-back-3" class="btn button-back btn-primary"
                                data-step_index="3"><span class="glyphicon glyphicon-backward"></span>
                            <?= lang('back') ?>
                        </button>
                        <button type="button" id="button-next-3" class="btn button-next btn-primary"
                                data-step_index="5">
                            <?= lang('next') ?>
                            <span class="glyphicon glyphicon-forward"></span>
                        </button>
                    </div>
                </div>