library(ggplot2)
library(gridExtra)
library(grid)

E_led <- c(
  0.0,
  1.443,
  1.646,
  1.695,
  1.720,
  1.742,
  1.759,
  1.788,
  1.820,
  1.842,
  1.866
)

I_F <- c(
  0.0,
  0.0113,
  0.86,
  2.855,
  4.736,
  6.95,
  8.99,
  12.77,
  17.65,
  21.37,
  25.84
)

data <- data.frame(E_led = E_led, I_F = I_F)

p1 <- ggplot(data, aes(x = E_led, y = I_F)) +
  geom_point(shape = 21, fill = "white") +
  geom_line() +
  xlab(expression(E["LED"] ~ "[V]")) +
  ylab(expression(I["F"] ~ "[mA]")) +
  theme_bw(base_family = "serif") +
  theme(
    text = element_text(family = "serif"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank()
  )

title <- textGrob(
  expression("Figure 1: - Current and Voltage Variations for LED:" ~ I["F"] ~ "[mA] versus" ~ E["LED"] ~ "[V]"),
  gp = gpar(fontsize = 14, fontfamily = "serif"),
  hjust = 0.5
)

p1_out <- grid.arrange(p1, title, ncol = 1, heights = c(10, 1))

ggsave(filename = "I_F vs E_LED plot.png", plot = p1_out, width = 8.5, height = 11)
