package com.dpet23.github.automation_googlesearch;

import android.annotation.SuppressLint;
import android.annotation.TargetApi;
import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.view.KeyEvent;
import android.view.View;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends Activity {

    private Button buttonStart;
    private Button buttonStop;
    private WebView webView;
    private TextView status;

    String URL = "https://www.google.com";
    List<String> USERAGENTS;
    Handler HANDLER;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Get UI elements
        buttonStart = (Button) findViewById(R.id.buttonStart);
        buttonStop = (Button) findViewById(R.id.buttonStop);
        webView = (WebView) findViewById(R.id.webView);
        status = (TextView)  findViewById(R.id.status);

        // Pretend to be Edge 41 on a Samsung Galaxy S8+ phone
        USERAGENTS = new ArrayList<String>();
        USERAGENTS.add("Mozilla/5.0 (Linux; Android 7.0; SM-G955F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36 EdgA/41.0.0.1561");

        // Set handler for delaying events
        HANDLER = new Handler();

        // When clicking the Start button
        buttonStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startSearch();
            }
        });

        // When clicking the Stop button
        buttonStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                stopSearch();
            }
        });

        // Show current status
        status.setText("Status: App open.");

        // To start the automation when the app opens
//        startSearch();
    }

    /**
     * Perform search automation.
     */
    @SuppressLint("SetJavaScriptEnabled")
    private void startSearch() {
        for (String useragent : USERAGENTS) {
            // Update status
            status.setText("Status: 'Start' button pressed.");

            // Set up browser
            webView.getSettings().setUserAgentString(useragent);
            webView.getSettings().setJavaScriptEnabled(true);
            Toast.makeText(MainActivity.this,
                    "Current useragent:" + "\n\n" + webView.getSettings().getUserAgentString(),
                    Toast.LENGTH_LONG).show();

            // Make page open in app's webview instead of browser
            webView.setWebViewClient(new WebViewClient() {
                @SuppressWarnings("deprecation")
                @Override
                public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
                    Toast.makeText(MainActivity.this, description, Toast.LENGTH_SHORT).show();
                }
                @TargetApi(android.os.Build.VERSION_CODES.M)
                @Override
                public void onReceivedError(WebView view, WebResourceRequest req, WebResourceError rerr) {
                    onReceivedError(view, rerr.getErrorCode(), rerr.getDescription().toString(), req.getUrl().toString());
                }
            });

            // Load URL
            status.setText("Status: Opening " + URL);
            webView.loadUrl(URL);

            // Enter search query
            HANDLER.postDelayed(new Runnable() {
                public void run() {
                    status.setText("Status: Entering query");
                    web_enter_text("q", "test search");
                }
            }, 10000); // wait 10 seconds for the page to load

            // Perform search
            HANDLER.postDelayed(new Runnable() {
                public void run() {
                    status.setText("Status: Pressing search button");
                    web_click_button("tsbb");
                }
            }, 15000); // wait another 5 seconds

            // Finish
            HANDLER.postDelayed(new Runnable() {
                public void run() {
                    Toast.makeText(MainActivity.this,
                            "Automation finished.\n\nWhen ready, press the 'Stop' button.",
                            Toast.LENGTH_LONG).show();
                    status.setText("Status: Automation finished.");
                }
            }, 20000); // wait another 5 seconds
        }
    }

    /**
     * Close the webview.
     */
    private void stopSearch() {
        webView.clearHistory();
        webView.clearCache(true);
        webView.loadUrl("about:blank");
//        webView.onPause();
//        webView.removeAllViews();
//        webView.destroyDrawingCache();
//        webView.destroy();
//        webView = null;
        Toast.makeText(MainActivity.this, "WebView stopped.", Toast.LENGTH_SHORT).show();
        status.setText("Status: WebView stopped.");
    }

    /**
     * Click on a web UI element in the webview using JavaScript.
     * @param id The web ID of the element to click on
     */
    private void web_click_button(String id) {
        // Send JavaScript to press a button
        webView.loadUrl("javascript:(function() {" +
                "var event = new MouseEvent('click', {" +
                "    view: window," +
                "    bubbles: true," +
                "    cancelable: true" +
                "  });" +
                "var element = document.getElementById('" + id + "');" +
                "element.dispatchEvent(event);" +
                "})()");
    }

    /**
     * Enter text in a textfield in the webview using JavaScript.
     * @param name The web name of the textfield
     * @param text The text to enter
     */
    private void web_enter_text(String name, String text) {
        // Focus on textfield
        webView.loadUrl("javascript:(function() {" +
                "document.getElementsByName('" + name + "')[0].focus();" +
                "})()");

        // Send JavaScript to enter text
        webView.loadUrl("javascript:(function() {" +
                "    document.getElementsByName('" + name + "')[0].value = '" + text + "';" +
                "})()");

        // To trigger the textfield's onchange event
        webView.dispatchKeyEvent(new KeyEvent(KeyEvent.ACTION_DOWN, KeyEvent.KEYCODE_SPACE));
        webView.dispatchKeyEvent(new KeyEvent(KeyEvent.ACTION_UP, KeyEvent.KEYCODE_SPACE));
        webView.dispatchKeyEvent(new KeyEvent(KeyEvent.ACTION_DOWN, KeyEvent.KEYCODE_DEL));
        webView.dispatchKeyEvent(new KeyEvent(KeyEvent.ACTION_UP, KeyEvent.KEYCODE_DEL));
    }
}
